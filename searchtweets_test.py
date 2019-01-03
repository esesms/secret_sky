#this is a test update

from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results

#load credentials
premium_search_args = load_credentials("~/.twitter_keys.yaml",
                                      yaml_key="search_tweets_premium",
                                      env_overwrite=False)

#search term
rule = gen_rule_payload("clouds taste like", results_per_call=100)
print(rule)

#search
tweets = collect_results(rule,
                        max_results=100,
                        result_stream_args=premium_search_args)

#output
#[print(tweet.all_text, end='\n\n') for tweet in tweets[0:10]];

#convert to string
tweet_str = ""

for tweet in tweets[20:30]:
    tweet_str += str(tweet.all_text)     
print(tweet_str)

#write to file
file = open("twitter_text.txt", "a")
file.write(tweet_str)
#file.write(str((tweets[1]).all_text))
file.close()