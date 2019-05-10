import tweepy
import pprint
'''	CONSTANTS '''
CLIENT_KEY = 'your key here'
CLIENT_SECRET = 'your secret hee'
ACCESS_TOKEN = 'acceess token here'
ACCESS_SECRET = 'acces secret here'
''' '''

''' AUTH HANDLERS '''
auth = tweepy.OAuthHandler(CLIENT_KEY, CLIENT_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

print(api.direct_messages(count=5)) #DM endpoint is ded like my will to live