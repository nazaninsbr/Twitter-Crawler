from textblob import TextBlob 
import tweepy
from tweepy import OAuthHandler
from general import *

TWITTER_DIRECTORY = 'Twitter/'
MAX_TWEETS = 1000

class Crawler:
	
	def __init__(self):
		self.api = ''
		self.consumer_key = ''
		self.consumer_secret = ''
		self.access_token = ''
		self.access_secret = ''
		self.createAPI()
		create_project_dir(TWITTER_DIRECTORY)

	def createAPI(self):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_secret)
		self.api = tweepy.API(auth) 

	def getTimeLine(self):
		allTimelines = ''
		for tweet in tweepy.Cursor(self.api.user_timeline).items():
			allTimelines = tweet.text+'<#@#>'
		create_data_files(TWITTER_DIRECTORY, 'timeline.txt', allTimelines)

	def searchTweets(self, keyword):
		public_tweets = self.api.search(keyword)
		self.WriteTweetToFile(keyword, public_tweets)
		return public_tweets

	def WriteTweetToFile(self, keyword, tweets):
		THIS_DIR = TWITTER_DIRECTORY+keyword+'/'
		create_project_dir(THIS_DIR)
		path = THIS_DIR+'allTweets.txt'
		for tweet in tweets:
			add_data_to_file(path, tweet.text+'<#@#>')

	def sentimentAnalysisOfTweet(self, tweets):
		for tweet in tweets:
			print(tweet.text)
			analysis = TextBlob(tweet.text)
			print(analysis.sentiment)

	def sentimentAnalysisOfFile(self, tweets):
		for tweet in tweets:
			print(tweet)
			analysis = TextBlob(tweet)
			print(analysis.sentiment)

	def readTweetsFromFile(self, keyword):
		path = TWITTER_DIRECTORY+keyword+'/allTweets.txt'
		content = []
		with open(path, 'r') as f:
			data = f.read()
			data = data.split('<#@#>')
			content = [x for x in data if not x=='']
		print(content)
		return content

	def searchHashtagTweets(self, keyword):
		hashtag = keyword
		count = 0
		HASHTAG_DIR = TWITTER_DIRECTORY +hashtag+'/'
		create_project_dir(HASHTAG_DIR)
		path = HASHTAG_DIR +'allTweets.txt'
		for tweet in tweepy.Cursor(self.api.search, q='#'+hashtag, rpp=100).items(MAX_TWEETS):
			count +=1
			add_data_to_file(path, tweet.text+'<#@#>')
		count = 0