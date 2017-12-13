# 507_FinalProject
For the final project of 507 i wanted to use the spotify API to select a track for the user based on their mood. The idea of the program is to find out what is the users favorite artist and how the user is feeling. If the user is feeling low the song help better the mood. If the user is already in a good mood the program support the emotion with something that is in synch with the

#Introduction
This project will pull data about the users favorite Artist and first look up the top 10 tracks of the artist. Next it collects information of the features of each of tracks of the artist. The features give an integer value of percentage of valence, tempo, liveliness, energy, danceability and the track. The database spotify_db collects all these elements including the track URl and uri information and stores it in tables. The tables are connected by the artist_id

#Part I - Getting Started - Downloading necessary files
Download the following files from this Github repository into the same folder on your desktop:
*SI507F17_finalproject.py* - the program file
*SI507F17_finalproject_tests.py* - These tests test the basic collection and functioning of the two classes to make sure the information collected at every stage is being processed correctly.
*config.py* - this is information for setting up your database(added to .gitignore)
*secret_data.py* - this is the secret information for Oauth (added to gitignore)
requirements.txt - this contains the necessary packages used for the code. You will need to install these packages for the code to work.
*template/*  - this folder contains the index html file for the falsk html visualization
*token.json* - this file should get created when you done the first run of the code. This ensures a cached oauth for a limited period of time so that you dont have to keep giving it access.

#Part II - Getting Started - Running the code
- We will be using Python3 for this project
- Create a virtual environment with python 3
- Pip install everything from the requirements.txt file
- Create a database on the terminal.The name of the database is in the config.py file
- On your terminal, to run the program, type, "python3 SI507F17_finalproject.py"
- use team SQL or a similar program to check the database tables

#Part III - What output to expect
- Once you run the code, you will notice that a web browser opens opening the Html page.
- the code also executes and prints a query which pulls the data for the html output.
- The print statements also show the .repr() methods of the artist object and the track object of all the top 10 tracks of that artist in your terminal.  
- you can interact with the html page to see results as attached
- In your database program you will find the tables keep adding the details for artist and tracks for everynew artist you say you like.
- The HTML plays the song that is selected based on the mood that you say your are feeling  

#Part IV - Resources used
I received assistance from Anand Doshi (class Graduate instructor) . I also used references from our class exercises and projects specifically for caching token for OAuth2,  calling queries in SQL and setting up database tables, and making html pages using flask.
