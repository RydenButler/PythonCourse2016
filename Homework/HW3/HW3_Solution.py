import tweepy
import time

UM = api.get_user('UMiamiDebate')

#Status count
UMTweets = UM.statuses_count

# Followers
UMFollowers = []
for user in TreatErrors(tweepy.Cursor(api.followers,'UMiamiDebate').items()):
     UMFollowers.append(user.screen_name)

# Most active follower
FollowT = Find_Tweets(UMFollowers)
Find_max(FollowT)

# Most followed follower
FollowF = Find_Followers(UMFollowers)
Find_max(FollowF)

# Followed
UMFriends = []
for user in TreatErrors(tweepy.Cursor(api.friends, 'UMiamiDebate').items()):
	UMFriends.append(user.screen_name)

# Most active friend; by category
FriendT = Find_Tweets(UMFriends)

Layman = {}
Expert = {}
Celebrity = {}
for friend in FriendT:
	if FriendT[friend] < 100:
		Layman[friend] = FriendT[friend]
	if FriendT[friend] > 1000: 
		Celebrity[friend] = FriendT[friend]
	else:
		Expert[friend] = FriendT[friend]

Find_max(Layman)
Find_max(Expert)
Find_max(Celebrity)

# Most followed friend
FriendF = Find_Followers(UMFriends)

Find_max(FriendF)

# Most active follower; by category
Layman_foll = {}
Expert_foll = {}
Celebrity_foll = {}
for follower in FollowT:
	if FollowT[follower] < 100:
		Layman_foll[follower] = FollowT[follower]
	if FollowT[follower] > 1000:
		Celebrity_foll[follower] = FollowT[follower]
	else:
		Expert_foll[follower] = FollowT[follower]

# Exclude celebrities for 2nd level analysis
Not_Celebs = Layman.copy()
Not_Celebs.update(Expert)
Not_Celebs = Not_Celebs.keys()

Not_Celebs_Foll = Layman_foll.copy()
Not_Celebs_Foll.update(Expert_foll)
Not_Celebs_Foll = Not_Celebs_Foll.keys()

# Most active follower of followers
Foll2 = Followers2(Not_Celebs_Foll)

Foll2_Tweets = {}
for i in Foll2:
	Foll2_Tweets.update(Find_Tweets(i))

Find_max(Foll2_Tweets)

# Most active friend of friends
Friend2 = Friends2(Not_Celebs)

Friend2_Tweets = {}
for i in Friend2:
	Friend2_Tweets.update(Find_Tweets(i))

Find_max(Friend2_Tweets)




def TreatErrors(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TweepError:
            time.sleep(20 * 60)

def Find_Tweets(User_List):
	User_Tweets = {}
	for user in User_List:
		username = str(user)
		while True:
			try:
				new_user = api.get_user(username)
				User_Tweets[username] =  new_user.statuses_count
				break
			except tweepy.TweepError:
				time.sleep(20 * 60)
	return User_Tweets

def Find_Followers(User_List):
	User_Followers = {}
	for user in User_List:
		username = str(user)
		while True:
			try:
				new_user = api.get_user(username)
				User_Followers[username] = new_user.followers_count
				break
			except tweepy.TweepError:
				time.sleep(20 * 60)
	return User_Followers

def Find_max(Dictionary):
	top_user = max(Dictionary, key=Dictionary.get)
	top_value = Dictionary[top_user]
	print '%s: %s' % (top_user, top_value)


def Followers2(Follower_List):
	All_Followers = []
	for follower in Follower_List:
		User_Followers = []
		for user in TreatErrors(tweepy.Cursor(api.followers,follower).items()):
			print user.screen_name
			User_Followers.append(user.screen_name)
		All_Followers.append(User_Followers)
	return All_Followers

def Friends2(Friend_List):
	All_Friends = []
	for friend in Friend_List:
		User_Friends = []
		for user in TreatErrors(tweepy.Cursor(api.friends, friend).items()):
			print user.screen_name
			User_Friends.append(user.screen_name)
		All_Friends.append(User_Friends)
	return All_Friends








