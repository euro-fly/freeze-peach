'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = '4SjCJAlWKQ3Pv3G396RWL5RAc'
MY_CONSUMER_SECRET = 'u7Cjqjcbp3q2duVfo3fT0jY77TPgyJzmJCNkvFVW7DFBHhBIPu'
MY_ACCESS_TOKEN_KEY = '796852642991345664-ACqAKDvsJ1QTgXJaqOLiSPe5QzGQOWc'
MY_ACCESS_TOKEN_SECRET = 'LQcwaGy0rq192TGpw2wdwVcMQR102qQtKIHWp6dsu71j6'

SOURCE_ACCOUNTS = ["hacaplus"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 0 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "hacaminus" #The name of the account you're tweeting to.
