import twint
#configuration
config = twint.Config()
config.Search = "#ParoDeTransportistas"
config.Limit = 10
#running search
twint.run.Search(config)
tlist = config.search_tweet_list
print(tlist)