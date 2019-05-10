import spotipy
import spotipy.util as util
import pprint

#CONSTANTS

CLIENT_ID = '74a7cfed9c0e434eac1a6ca56d9e41e8'
CLIENT_SECRET = '1408599c0ce24a1c90cb3e35b40418c1'
PLAYLIST_NAME = "Name the playlist"
USERNAME = "bhavdeep2533"
PLAYLSIT_ID = 'playlist ID here'
''' '''
#AUTH MANAGER
token = util.prompt_for_user_token(
        username= USERNAME,
        scope= 'user-library-read',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri='http://localhost/callback')

spotify = spotipy.Spotify(auth=token)

#Get user's saved tracks, save it in a 'tracks' list
tracks = spotify.current_user_saved_tracks()['items']

tracksToBeAdded = []
i = 0
temp = tracks[i]

#Find the cutoff and add the ID's of songs to be added to a separate list 
#Example song, Nyquist by deadmau5
while not (temp['track']['name'].lower() == 'nyquist') and  not (i == 20):
	#print(temp['track']['name'].lower())
	temp = tracks[i]	
	tracksToBeAdded.append(temp['track']['id'])
	i += 1

#print(len(tracksToBeAdded))
#Search user's playlists to see which one they want to store it in
#Example Playlist, playlistmeister
j = 0 
playListID = 0
for f in spotify.current_user_playlists()['items']:
	if f['name'].lower() == 'playlistmeister':
		playListID = f['id']

#Implement the copy, appends to the playlist, provided everything is found
spotify.user_playlist_add_tracks(USERNAME, playListID, tracksToBeAdded)

print("Done")
