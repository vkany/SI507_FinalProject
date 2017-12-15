# import indico.io
from secret_data import *
import requests_oauthlib
from requests_oauthlib import OAuth2Session
import webbrowser
import json
import random
import psycopg2
import psycopg2.extras
from psycopg2 import sql
import sys
import operator
from config import *
from flask import Flask, request, render_template
import requests

db_connection = None
db_cursor = None


CLIENT_ID = CLIENT_ID  #'get this from spotify or create a secret data file, see spotify_data.py
CLIENT_SECRET = CLIENT_SECRET #'get this from spotify or create a secret data file, see spotify_data.py
AUTHORIZATION_URL = 'https://accounts.spotify.com/authorize'
# NOTE: you need to specify this same REDIRECT_URI in the Spotify API console of your application!
REDIRECT_URI = 'https://www.programsinformationpeople.org/runestone/oauth' # This is a URL we have specifically set up at UMSI to handle student requests, basically -- it is an "OAuth2 workaround". You could use any URL -- but it would be a bit rude to, because that's still a hit on someone's URL! In general, you'd use your own -- on your own server.
TOKEN_URL = 'https://accounts.spotify.com/api/token'
spotify_session = None

display = Flask(__name__)

CACHE_FNAME = 'cache_spotify.json'
try:
    cache_spotify = open(CACHE_FNAME, 'r')
    cache_contents = cache_spotify.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_spotify.close()
except:
    CACHE_DICTION = {}

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)
# Opening auth URL for you to sign in to the Spotify service
def execute(query, values=None):
    conn, cur = get_connection_and_cursor()
    cur.execute(query, values)
    results = cur.fetchall()
    return results

@display.route('/')
def index():
    # your_feeling = input("how are you feeling? (angry, sad, stressed,happy)\n")
    # artist = input("who is your favourite Artist/Album?\n")
    your_feeling = request.args.get('your_feeling')
    artist = request.args.get('artist')
    url = None

    if your_feeling and artist:

        # artist_id = artist_dict['id']
        artist_results = make_spotify_request('https://api.spotify.com/v1/search',params ={'q':artist,'type':'artist'})
        artist_dict = artist_results
        print(artist_dict)
        artist_obj = Artist(artist_dict)
        # artist.insert_into_database()
        print(artist_obj.__repr__())
        artist_obj.insert()
        top_tracks = artist_obj.get_top_tracks()
        # print(top_tracks.__repr__())
        for track_dict in top_tracks:
            track = Track(track_dict, artist_obj.artist_id)
            track.track_name
            track.get_features()
            track.insert()
            print(track.__repr__())

        selected_songs = get_dominant_feature(artist_obj.artist_id,your_feeling)
        song = random.choice(selected_songs)

        url = 'https://open.spotify.com/embed?uri={0}'.format(song['track_uri'])

        db_connection.commit()


    # always looks for template in 'templates' folder relative to the current folder
    return render_template('index.html', url=url)

def get_dominant_feature(artist_id,your_feeling):

    feeling_relation = {'angry':'liveliness', 'sad':'tempo', 'stressed':'energy','happy':'danceability'}
    # message_code = {'angry':["Cheer up!","It can only get better from here!","Hey buddy hang in there!It going to be fine!"],'happy':["Lets get that already great mood even better!","wooop! woop!","Hope this song just makes your mood even bette!"] ,'sad':["Cheer up!","You are going to get through this!","I am sorry! hope you feel better soon!"],'sad':["Oh no!","I am so sorry about this news","It's going to be okay!"],'surprise':["I know this sucks", "Just as shocked","Oh my!"]}

    return execute("""
        select "track_name", "track_url", "track_uri"
        from Track
        where
            ("artist_id" = %s)
            and (
                "{0}" >= (SELECT avg("{0}") FROM Track WHERE "artist_id" = %s)
            )
        """.format(feeling_relation[your_feeling]), (artist_id, artist_id))

def make_spotify_request(url, params=None):
    if not params:
        params = {}

    # we use 'global' to tell python that we will be modifying this global variable
    global spotify_session

    if not spotify_session:
        start_spotify_session()

    unique_ident = params_unique_combination(url,params)
    if unique_ident in CACHE_DICTION:
        # print('--from-cache--')
        return CACHE_DICTION[unique_ident]
    else:
        resp = spotify_session.get(url, params=params)

        CACHE_DICTION[unique_ident] = json.loads(resp.text)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[unique_ident]


def start_spotify_session():
    global spotify_session

    # 0 - get token from cache
    try:
        token = get_saved_token()
    except FileNotFoundError:
        token = None

    if token:
        spotify_session = OAuth2Session(CLIENT_ID, token=token)
    else:
        # 1 - session
        spotify_session = requests_oauthlib.OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI) # Create an instance of an OAuth2Session
        authorization_url, state = spotify_session.authorization_url(AUTHORIZATION_URL)
        r = spotify_session.get('https://api.spotify.com/v1/')
        response_diction = json.loads(r.text)
        print(json.dumps(response_diction, indent=2))
        print('Opening browser to {} for authorization'.format(authorization_url))
        webbrowser.open(authorization_url)
        #2 Authenticate
        authorization_response = input('Authenticate and then enter the full callback URL: ').strip() # Need to get the full URL in order to parse the response
        # 3 - token
        token = spotify_session.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET,authorization_response=authorization_response)
        # 4 - save token
        save_token(token)

def get_saved_token():
    with open('token.json', 'r') as f:
        token_json = f.read()
        token_dict = json.loads(token_json)
        return token_dict

def save_token(token_dict):
    with open('token.json', 'w') as f:
        token_json = json.dumps(token_dict)
        f.write(token_json)

def get_connection_and_cursor():
    global db_connection, db_cursor
    if not db_connection:
        try:
            db_connection = psycopg2.connect("dbname='{0}' user='{1}' password='{2}'".format(db_name, db_user, db_password))
            print("Success connecting to database")
        except:
            print("Unable to connect to the database. Check server and credentials.")
            sys.exit(1) # Stop running program if there's no db connection.

    if not db_cursor:
        db_cursor = db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    return db_connection, db_cursor

def setup_database():
    conn, cur = get_connection_and_cursor()

    # cur.execute("drop table if exists Track")
    # cur.execute("drop table if exists Artist")

    #Create Artist table
    cur.execute("""CREATE TABLE IF NOT EXISTS Artist(
    artist_id VARCHAR(255) PRIMARY KEY,
    artist_name VARCHAR(255) NOT NULL
     )""")
    # cur.execute("DROP TABLE IF EXISTS Artists")
    # Create Track table
    cur.execute("""CREATE TABLE IF NOT EXISTS Track(
    track_id VARCHAR(255) PRIMARY KEY,
    artist_id VARCHAR(255) REFERENCES Artist(artist_id) ,
    track_name VARCHAR(255) NOT NULL,
    track_url TEXT,
    track_uri TEXT,
    danceability REAL,
    energy REAL,
    liveliness REAL,
    tempo REAL
    )""")

    conn.commit()
    print('Setup database complete')

def insert(table, data_dict):
    """Accepts connection and cursor, table name, dictionary that represents one row, and inserts data into table. (Not the only way to do this!)"""
    conn, cur = get_connection_and_cursor()
    column_names = data_dict.keys()
    # print(column_names, "column_names") # for debug
    query = sql.SQL('INSERT INTO {0}({1}) VALUES({2}) ON CONFLICT DO NOTHING').format(
        sql.SQL(table),
        sql.SQL(', ').join(map(sql.Identifier, column_names)),
        sql.SQL(', ').join(map(sql.Placeholder, column_names)),
    )
    query_string = query.as_string(conn) # thanks to sql module
    cur.execute(query_string, data_dict) # will mean that id is in cursor, because insert statement returns id in this function

# insert('Artist', {'artist_id': self.artist_id, ...})
# insert('Track', {'column_name': 'value', ...})

class Artist:
    def __init__(self, artist_dict):
        self.artist_id = artist_dict['artists']['items'][0]['id']
        self.artist_name = artist_dict['artists']['items'][0]['name']

    def get_top_tracks(self):
        # artist_request = make_spotify_request('https://api.spotify.com/v1/artists/{0}'.format(self.artist_id))
        top_tracks_url = 'https://api.spotify.com/v1/artists/{0}/top-tracks'.format(self.artist_id)
        top_tracks_dict = make_spotify_request(top_tracks_url, params={'country':"US"})
        self.top_tracks_list = top_tracks_dict['tracks']
        return self.top_tracks_list

    def insert(self):
        row = {
            'artist_name': self.artist_name,
            'artist_id': self.artist_id
        }
        insert('Artist', row)



    def __repr__(self):
        return "<Artist object for {1} with id {0}>".format(self.artist_id, self.artist_name)


class Track:
    def __init__(self, track_dict, artist_id):
        self.track_id = track_dict['id']
        self.track_name = track_dict['name']
        self.track_url = track_dict['href']
        self.track_uri = track_dict['uri']
        self.artist_id = artist_id
        self.track_dict = track_dict

    def get_features(self):
        features = make_spotify_request('https://api.spotify.com/v1/audio-features/{}'.format(self.track_id))
        self.features_dict = features
        # self.track_name = self.track_name
        self.liveness = self.features_dict['liveness']
        self.danceability = self.features_dict['danceability']
        self.energy = self.features_dict['energy']
        self.tempo = self.features_dict['tempo']

    def insert(self):
        row = {
            "track_id" : self.track_id,
            "artist_id": self.artist_id,
            "track_name": self.track_name,
            "track_url": self.track_url,
            "track_uri": self.track_uri ,
            "danceability": self.danceability,
            "energy": self.energy,
            "liveliness": self.liveness,
            "tempo": self.tempo
        }
        insert('Track', row)

    def __repr__(self):
        return "<Track object '{}' has {} liveliness, {} energy, and {} danceability>".format(self.track_name, self.liveness, self.energy, self.danceability)

    def __contains__(self, aword):
        self.aword = aword
        return self.aword in self.track_name




    # track.insert_into_database()
    # get sentiment



if __name__ == '__main__':
    setup_database()
    # auto reloads (mostly) new code and shows exception traceback in the browser
    display.run(use_reloader=True, debug=True)
