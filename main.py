from sys import argv
from crawler import Crawler

def mainFunc():
	t_crawler = Crawler()
	if '--timeline' in argv:
		t_crawler.getTimeLine()
	elif '--hashtagSearch' in argv:
		t_crawler.searchHashtagTweets(argv[2])
	elif '--search' in argv:
		t_crawler.searchTweets(argv[2])
	elif '--sentiment' in argv:
		if '--crawl' in argv:
			tweets = t_crawler.searchTweets(argv[3])
			t_crawler.sentimentAnalysisOfTweet(tweets)
		elif '--file' in argv:
			tweets = t_crawler.readTweetsFromFile(argv[3])
			t_crawler.sentimentAnalysisOfFile(tweets)
	elif '--file' in argv:
		 t_crawler.readTweetsFromFile(argv[2])

if __name__ == '__main__':
	mainFunc()