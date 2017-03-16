import twitter
import warnings
import time

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

#print api.VerifyCredentials()

b = open('nazis.txt')
b2 = b.read().decode("utf-8-sig").encode("utf-8")
bigbads = b2.split("\n")
bigbads.pop()
badslist = dict()

for bad in bigbads:
    #print bad
    try:
        
        baddie = api.GetUser(screen_name=bad)
        source = baddie.screen_name
        print "Blocking user " + source
        api.CreateBlock(screen_name = source)
        print "Successfully blocked!"
        badslist[baddie.id] = True
        try:
            bad_follows = api.GetFollowersPaged(screen_name = source)
            while True:
                next_cursor = bad_follows[0]
                print "Retrieved a batch of " + str(len(bad_follows)) + " followers."
                for follow in bad_follows[2]:
                    try:
                        #print "Checking status of user " + follow.screen_name + "..."
                        if follow.id not in badslist:
                            badslist[follow.id] = True
                        else:
                            print "Blocking user " + follow.screen_name
                            api.CreateBlock(screen_name=follow.screen_name)
                            print "Successfully blocked!"
                    except:
                        print "Something bad happened when we tried to process a follower."
                if (next_cursor == 0):
                    break
                else:
                    print "Sleeping..."
                    time.sleep(10)
                    bad_follows = api.GetFollowersPaged(screen_name = source, cursor=next_cursor)
                
        except:
            print "We couldn't get the followers..."
        
    except:
        print "Error, we couldn't get user data for that baddie."
