import tweepy
import time

# 1-degree: most active, followers, active layman/expert/celebrity followed, popular followed
# 2-degree: of followers-followers most active, following-following most active

api.rate_limit_status()

UM = api.get_user('UMiamiDebate')

UMTweets = UM.statuses_count





UMFollowers = []
for user in TreatErrors(tweepy.Cursor(api.followers,'UMiamiDebate').items()):
     UMFollowers.append(user.screen_name)

FollowT = Find_Tweets(UMFollowers)
max(FollowT, key=FollowT.get) # EP_Mundo
FollowT['EP_Mundo'] # 990827

FollowF = Find_Followers(UMFollowers)
max(FollowF, key=FollowF.get) # EP_Mundo
FollowF['EP_Mundo'] # 543858

UMFriends = []
for user in TreatErrors(tweepy.Cursor(api.friends, 'UMiamiDebate').items()):
	UMFriends.append(user.screen_name)

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

max(Layman, key=Layman.get) # BSUDebate
Layman['BSUDebate'] # 95

max(Expert, key=Expert.get) # DebateCoaches
Expert['DebateCoaches'] # 993

max(Celebrity, key=Celebrity.get) # UniNoticias
Celebrity['UniNoticias'] # 127945

FriendF = Find_Followers(UMFriends)

max(FriendF, key=FriendF.get) # Dropbox
FriendF['Dropbox'] # 4452970

Foll2 = Followers2(UMFollowers)



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

def Followers2(Follower_List):
	All_Followers = []
	for follower in Follower_List:
		User_Followers = []
		for user in TreatErrors(tweepy.Cursor(api.followers,follower).items()):
			User_Followers.append(user.screen_name)
		All_Followers.append(User_Followers)
	return All_Followers







