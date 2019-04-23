import spotipy
import spotipy.util as util
import pprint

''' CONSTANTS '''

CLIENT_ID = 'your ID here'
CLIENT_SECRET = 'your secret here'
PLAYLIST_NAME = "Name the playlist"
USERNAME = "username here"
PLAYLSIT_ID = 'playlist ID here'
''' '''
''' AUTH MANAGER '''
token = util.prompt_for_user_token(
        username= USERNAME,
        scope= 'playlist-modify-public',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri='http://localhost/callback')

#client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
spotify = spotipy.Spotify(auth=token)
''' '''
songs = []
#adding Vegas Skies by THe Cab to the playlist
songs.append(spotify.track('https://open.spotify.com/track/42zAWdwkrkufVDDdAXoubu?si=pv_vA7dPSkS_OzXt2KirVA')['id'])

#playlist = spotify.user_playlist_create(user=USERNAME, name=PLAYLIST_NAME, public=True)
playlist = spotify.user_playlist(user=USERNAME, playlist_id=PLAYLSIT_ID)
spotify.user_playlist_add_tracks(user=USERNAME, playlist_id=PLAYLSIT_ID, tracks=songs, position=None)

pprint.pprint(playlist)

songs.clear()