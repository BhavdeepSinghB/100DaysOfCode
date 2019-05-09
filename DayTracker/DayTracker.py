import tweepy

#Constants
KEY = '#'
KEY_SECRET = '#'
TOKEN = '#'
TOKEN_SECRET = '#'
FILENAME = 'day.txt'
MAX_CHARS = 280


#Check if Tweet size is too big
#Size is a separate variable because Of links, which just add 23 chars
def legalTweetSize(size):
	if size > MAX_CHARS:
		return False
	return True

#Connect to API

auth = tweepy.OAuthHandler(KEY, KEY_SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)

api = tweepy.API(auth)


#If Successful, read file for the current day's update
fh = open(FILENAME, "r")

day = fh.read()
numday = int(day)

fh.close()

tweetString = "#100DaysOfCode\nDay " + day + ": "

userString = input('Enter the tweet: ')
tweetString += userString

tweetSize = len(tweetString)

while not legalTweetSize(tweetSize):
	print(tweetString + "\nIs not a valid tweet, please shorten it by " + str(tweetSize - MAX_CHARS) + " characters")
	userString = input("Enter the tweet: ")
	tweetString = "#100DaysOfCode\nDay " + day + ": " + userString
	tweetSize = len(tweetString)

tweetClone = tweetString

urlAsker = input("Add URL? (y/n) ")
if urlAsker.lower() == "y":
	tweetSize += 24
	if not legalTweetSize(tweetSize):
		urlChecker = input("Too much text\nPress y to change, n to remove URl")
		if(urlChecker.lower=='y'):
			 while not legalTweetSize(tweetSize):
			 	print(tweetString + "\nIs not a valid tweet, please shorten it by " + str(tweetSize - (MAX_CHARS - 23)) + " characters")
			 	userString = input("Enter the tweet: ")
			 	tweetString = "#100DaysOfCode\nDay " + day + ": " + userString
			 	tweetSize = len(tweetString) + 24
	#Approved to add URL, ask what kind
	url = input("100DaysOfCode url? (Y/N) ")
	if url == "y":
		tweetString += "\nhttps://www.github.com/BhavdeepSinghB/100DaysOfCode/"
	else:
		tweetString += input("Enter other URL: ")

#If everything works, we can post a tweet
api.update_status(tweetString)

numday += 1

fh = open(FILENAME, "w")
fh.write(numday)
fh.close()
 




