import tweepy

auth = tweepy.OAuthHandler('Xw01gAQNSwJmfPvzbDWbcEa8G', 'Dygo13v2N8kQWoDSZ6LMgX7gk7rJKgaxkuCjBoP1dFVJTh73Qa')
auth.set_access_token('16540577-wvGdB7rBiJi9SJsDWYbS1VqCZj3ce1qn6RxZWDsss', '6jiSrxtYaXMoMr6XlGDG0jts7nvRe3KwGb4sLKF3s9Twv')

api = tweepy.API(auth)

#update status
#api.update_status('Hello Python!')

#output tweets in my home timeline
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

#search term option
#q="clouds AND \"taste like\"",

#searches twitter for
for tweet in tweepy.Cursor(api.search,
                           q="\"clouds taste\"",
                           count=100,
                           result_type="mixed",
                           include_entities=True,
                           lang="en").items(100):
    print(tweet.text)
    #print(tweet)