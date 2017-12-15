import unittest
from SI507F17_finalproject import *

###########


class Artist_test(unittest.TestCase):
    def setUp(self):
        self.a_dict = {'artists': {'href': 'https://api.spotify.com/v1/search?query=98+degrees&type=artist&market=US&offset=0&limit=20', 'items': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6V03b3Y36lolYP2orXn8mV'}, 'followers': {'href': None, 'total': 84708}, 'genres': ['dance pop'], 'href': 'https://api.spotify.com/v1/artists/6V03b3Y36lolYP2orXn8mV', 'id': '6V03b3Y36lolYP2orXn8mV', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/724da94d50ed555288c2fcf3cfd82e900c6fd0c0', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/8ec5c707c8bbf68f8803bff6040f79aab59c1850', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/23672431cdd798b63513765c5e411d8efbbe3a5a', 'width': 160}], 'name': '98º', 'popularity': 66, 'type': 'artist', 'uri': 'spotify:artist:6V03b3Y36lolYP2orXn8mV'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/7aEqjTBeH2YseqpfRUKeTZ'}, 'followers': {'href': None, 'total': 10}, 'genres': [],'href': 'https://api.spotify.com/v1/artists/7aEqjTBeH2YseqpfRUKeTZ', 'id': '7aEqjTBeH2YseqpfRUKeTZ', 'images': [], 'name': 'Joe & 98 Degrees', 'popularity': 0,'type': 'artist', 'uri': 'spotify:artist:7aEqjTBeH2YseqpfRUKeTZ'}], 'limit': 20, 'next': None, 'offset': 0, 'previous': None, 'total': 2}}
        self.degrees = Artist(self.a_dict)

    def test_artist_name_1(self):
        self.assertEqual(self.degrees.artist_name,"98º" )

    def test_type_2(self):
        self.assertEqual(type(self.degrees.artist_id),str)

    def test_artist_3(self):
        self.assertEqual(self.degrees.artist_id,"6V03b3Y36lolYP2orXn8mV")

    def test_repr_4(self):
        self.assertEqual(self.degrees.__repr__(),"<Artist object for 98º with id 6V03b3Y36lolYP2orXn8mV>" )

    def tearDown(self):
        self.a_dict
        self.degrees


class Track_test(unittest.TestCase):
    def setUp(self):
        self.a_dict1 = {'artists': {'href': 'https://api.spotify.com/v1/search?query=98+degrees&type=artist&market=US&offset=0&limit=20', 'items': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6V03b3Y36lolYP2orXn8mV'}, 'followers': {'href': None, 'total': 84708}, 'genres': ['dance pop'], 'href': 'https://api.spotify.com/v1/artists/6V03b3Y36lolYP2orXn8mV', 'id': '6V03b3Y36lolYP2orXn8mV', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/724da94d50ed555288c2fcf3cfd82e900c6fd0c0', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/8ec5c707c8bbf68f8803bff6040f79aab59c1850', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/23672431cdd798b63513765c5e411d8efbbe3a5a', 'width': 160}], 'name': '98º', 'popularity': 66, 'type': 'artist', 'uri': 'spotify:artist:6V03b3Y36lolYP2orXn8mV'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/7aEqjTBeH2YseqpfRUKeTZ'}, 'followers': {'href': None, 'total': 10}, 'genres': [],'href': 'https://api.spotify.com/v1/artists/7aEqjTBeH2YseqpfRUKeTZ', 'id': '7aEqjTBeH2YseqpfRUKeTZ', 'images': [], 'name': 'Joe & 98 Degrees', 'popularity': 0,'type': 'artist', 'uri': 'spotify:artist:7aEqjTBeH2YseqpfRUKeTZ'}], 'limit': 20, 'next': None, 'offset': 0, 'previous': None, 'total': 2}}
        self.degrees = Artist(self.a_dict1)
        self.a_dict2 =({'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6V03b3Y36lolYP2orXn8mV'}, 'href': 'https://api.spotify.com/v1/artists/6V03b3Y36lolYP2orXn8mV', 'id': '6V03b3Y36lolYP2orXn8mV', 'name': '98º', 'type': 'artist', 'uri': 'spotify:artist:6V03b3Y36lolYP2orXn8mV'}], 'available_markets': ['AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IS', 'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'SE', 'SG', 'SK', 'SV', 'TH', 'TR', 'TW', 'US', 'UY', 'VN'], 'external_urls': {'spotify': 'https://open.spotify.com/album/39FfOWdtZLLY1lMn2R3UIm'}, 'href': 'https://api.spotify.com/v1/albums/39FfOWdtZLLY1lMn2R3UIm', 'id': '39FfOWdtZLLY1lMn2R3UIm', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/568489a3dd31af57f18110d2c21543a9e240a11c', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/b8e0057be487d420df15f7225074bb2202f6f025', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/316a8f98c958ef1b9cac362c06d3e20446a15e69', 'width': 64}], 'name': '98º And Rising', 'type': 'album', 'uri': 'spotify:album:39FfOWdtZLLY1lMn2R3UIm'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6V03b3Y36lolYP2orXn8mV'}, 'href': 'https://api.spotify.com/v1/artists/6V03b3Y36lolYP2orXn8mV', 'id': '6V03b3Y36lolYP2orXn8mV', 'name': '98º', 'type': 'artist', 'uri': 'spotify:artist:6V03b3Y36lolYP2orXn8mV'}], 'available_markets': ['AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR', 'CA', 'CH', 'CL','CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IS', 'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'SE', 'SG', 'SK', 'SV', 'TH', 'TR','TW', 'US', 'UY', 'VN'], 'disc_number': 1, 'duration_ms': 226733, 'explicit': False, 'external_ids': {'isrc': 'USMO19883529'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/0p5Bv16XNo5B7AdeKD0H0F'}, 'href': 'https://api.spotify.com/v1/tracks/0p5Bv16XNo5B7AdeKD0H0F','id': '0p5Bv16XNo5B7AdeKD0H0F', 'name': 'I Do (Cherish You)', 'popularity': 51, 'preview_url': 'https://p.scdn.co/mp3-preview/4766ed59276f03619566cbcd79b32e428306e2f8?cid=98933bd11380400297c5a5ef67a59fb3', 'track_number': 4, 'type': 'track', 'uri': 'spotify:track:0p5Bv16XNo5B7AdeKD0H0F'})
        self.christmas = Track(self.a_dict2,self.degrees.artist_id)
        self.christmas.get_features()

    def test_dict_type_5(self):
        self.assertEqual(type(self.christmas.features_dict),dict)

    def test_get_top_tracks_6(self):
        self.assertEqual(len(self.christmas.features_dict.keys()),18)

    def test_number_of_tracks_7(self):
        self.assertEqual(type(self.christmas.track_dict),dict)

    def test_track_object_repr_8(self):
        self.assertEqual(self.christmas.__repr__(), "<Track object 'I Do (Cherish You)' has 0.144 liveliness, 0.441 energy, and 0.574 danceability>")

    def test_track_conatains_9(self):
        self.assertTrue(self.christmas.__contains__('Cheris')==True)

    def test_artist_id_matches_10(self):
        self.assertTrue(self.christmas.artist_id, self.degrees.artist_id)

    def test_trackname_11(self):
        self.assertEqual(self.christmas.track_name, "I Do (Cherish You)" )

    def test_track_uri_12(self):
        self.assertEqual(self.christmas.track_uri,'spotify:track:0p5Bv16XNo5B7AdeKD0H0F')

    def test_trackid_13(self):
        self.assertEqual(self.christmas.track_id,'0p5Bv16XNo5B7AdeKD0H0F')

    def test_trackurl_14(self):
        self.assertEqual(self.christmas.track_url,"https://api.spotify.com/v1/tracks/0p5Bv16XNo5B7AdeKD0H0F")

    def test_daceibility_15(self):
        self.assertEqual(type(self.christmas.danceability),float)

    def tearDown(self):
        self.a_dict1 = {'artists': {'href': 'https://api.spotify.com/v1/search?query=98+degrees&type=artist&market=US&offset=0&limit=20', 'items': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6V03b3Y36lolYP2orXn8mV'}, 'followers': {'href': None, 'total': 84708}, 'genres': ['dance pop'], 'href': 'https://api.spotify.com/v1/artists/6V03b3Y36lolYP2orXn8mV', 'id': '6V03b3Y36lolYP2orXn8mV', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/724da94d50ed555288c2fcf3cfd82e900c6fd0c0', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/8ec5c707c8bbf68f8803bff6040f79aab59c1850', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/23672431cdd798b63513765c5e411d8efbbe3a5a', 'width': 160}], 'name': '98º', 'popularity': 66, 'type': 'artist', 'uri': 'spotify:artist:6V03b3Y36lolYP2orXn8mV'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/7aEqjTBeH2YseqpfRUKeTZ'}, 'followers': {'href': None, 'total': 10}, 'genres': [],'href': 'https://api.spotify.com/v1/artists/7aEqjTBeH2YseqpfRUKeTZ', 'id': '7aEqjTBeH2YseqpfRUKeTZ', 'images': [], 'name': 'Joe & 98 Degrees', 'popularity': 0,'type': 'artist', 'uri': 'spotify:artist:7aEqjTBeH2YseqpfRUKeTZ'}], 'limit': 20, 'next': None, 'offset': 0, 'previous': None, 'total': 2}}
        self.degrees = Artist(self.a_dict1)
        self.a_dict2 =({'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6V03b3Y36lolYP2orXn8mV'}, 'href': 'https://api.spotify.com/v1/artists/6V03b3Y36lolYP2orXn8mV', 'id': '6V03b3Y36lolYP2orXn8mV', 'name': '98º', 'type': 'artist', 'uri': 'spotify:artist:6V03b3Y36lolYP2orXn8mV'}], 'available_markets': ['AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IS', 'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'SE', 'SG', 'SK', 'SV', 'TH', 'TR', 'TW', 'US', 'UY', 'VN'], 'external_urls': {'spotify': 'https://open.spotify.com/album/39FfOWdtZLLY1lMn2R3UIm'}, 'href': 'https://api.spotify.com/v1/albums/39FfOWdtZLLY1lMn2R3UIm', 'id': '39FfOWdtZLLY1lMn2R3UIm', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/568489a3dd31af57f18110d2c21543a9e240a11c', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/b8e0057be487d420df15f7225074bb2202f6f025', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/316a8f98c958ef1b9cac362c06d3e20446a15e69', 'width': 64}], 'name': '98º And Rising', 'type': 'album', 'uri': 'spotify:album:39FfOWdtZLLY1lMn2R3UIm'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6V03b3Y36lolYP2orXn8mV'}, 'href': 'https://api.spotify.com/v1/artists/6V03b3Y36lolYP2orXn8mV', 'id': '6V03b3Y36lolYP2orXn8mV', 'name': '98º', 'type': 'artist', 'uri': 'spotify:artist:6V03b3Y36lolYP2orXn8mV'}], 'available_markets': ['AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR', 'CA', 'CH', 'CL','CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IS', 'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'SE', 'SG', 'SK', 'SV', 'TH', 'TR','TW', 'US', 'UY', 'VN'], 'disc_number': 1, 'duration_ms': 226733, 'explicit': False, 'external_ids': {'isrc': 'USMO19883529'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/0p5Bv16XNo5B7AdeKD0H0F'}, 'href': 'https://api.spotify.com/v1/tracks/0p5Bv16XNo5B7AdeKD0H0F','id': '0p5Bv16XNo5B7AdeKD0H0F', 'name': 'I Do (Cherish You)', 'popularity': 51, 'preview_url': 'https://p.scdn.co/mp3-preview/4766ed59276f03619566cbcd79b32e428306e2f8?cid=98933bd11380400297c5a5ef67a59fb3', 'track_number': 4, 'type': 'track', 'uri': 'spotify:track:0p5Bv16XNo5B7AdeKD0H0F'})
        self.christmas = Track(self.a_dict2,self.degrees.artist_id)


if __name__ == '__main__':
    unittest.main(verbosity=2)
