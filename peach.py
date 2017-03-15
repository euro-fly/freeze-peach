import twitter
import warnings

warnings.filterwarnings("ignore")

MY_CONSUMER_KEY = "Ap1ok8lEFoWkPc4vTlapwpahv"
MY_CONSUMER_SECRET = "JoaUdPDaeFJA4CZCt5u5IvvmHpd2ltbtFXls7DwYUX7Qd7THgE"
MY_ACCESS_TOKEN_KEY = "841890782227386369-hybolyBqDLaIBR8AKmD4ExNFkg6I8Od"
MY_ACCESS_TOKEN_SECRET = "oBOsY2VgeZ6l1uJRTiQiIEO08lBN8SM33EUbfq0Qc2g3F"


# spin up a twitter api instance

api = twitter.Api(consumer_key=MY_CONSUMER_KEY,
                  consumer_secret=MY_CONSUMER_SECRET,
                  access_token_key=MY_ACCESS_TOKEN_KEY,
                  access_token_secret=MY_ACCESS_TOKEN_SECRET,
                  sleep_on_rate_limit=True)

b = open('nazis.txt')
b2 = b.read().decode("utf-8-sig").encode("utf-8")
bigbads = b2.split("\n")
bigbads.pop()
badslist = dict()

for bad in bigbads:
    #print bad
    try:
        
        baddie = api.GetUser(screen_name=bad)
        print "Blocking user " + baddie.screen_name
        api.CreateBlock(screen_name = baddie.screen_name)
        try:
            bad_follows = api.GetFollowers(screen_name = baddie.screen_name)
            badslist[baddie.user_id] = True
            for follow in bad_follows:
                try:
                    print "Checking status of user " + follow.screen_name + "..."
                    if follow.id not in badslist:
                        badslist[follow.id] = True
                    else:
                        print "Blocking user " + follow.screen_name
                        api.CreateBlock(screen_name=follow.screen_name)
                except:
                    print "Something bad happened when we tried to process a follower."
        except:
            print "We couldn't get the followers..."
        
    except:
        print "Error, we couldn't get user data for that baddie."
        pass
