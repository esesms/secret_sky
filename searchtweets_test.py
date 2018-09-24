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
[print(tweet.all_text, end='\n\n') for tweet in tweets[0:10]];