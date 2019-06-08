import spotipy
import spotipy.util as util
from pprint import pprint

#constants
CLIENT_ID = '#'
CLIENT_SECRET = '#'
USERNAME = 'bhavdeep2533'

#auth manager
token = util.prompt_for_user_token(
        username= USERNAME,
        scope= 'user-follow-read',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri='http://localhost/callback')

spotify = spotipy.Spotify(auth=token)

#main
me = spotify.me()
followed = spotify.current_user_followed_artists()
pprint(spotify.user_playlist('xw85oi25jzsuwj4ll4bz8moht'))
