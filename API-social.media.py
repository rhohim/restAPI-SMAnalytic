import instaloader
 
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
# bot.login(user="getpc_os",passwd="Minimal8.") #Use this code to log-in to your account.

profileid = "cretivox"
# Loading the profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, profileid)
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)   
print('\n')
num_followers = profile.followers
total_num_likes = 0
total_num_comments = 0
total_num_posts = 0
valueA, datapost = [] , []
truncA = 0
i = 0
for post in profile.get_posts():
    total_num_likes += post.likes
    total_num_comments += post.comments
    total_num_posts += 1
    print(i)
    # print(post.url)
    # print(post.comments)
    # print(post.likes)
    post = {
        "url_post_"+ str(i): post.url,
        "like_"+ str(i) : post.likes,
        "comment_"+ str(i): post.comments
    }
    datapost.append(post)
    engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
    valueA.append(engagement * 100)
    
    if i == 11:
        ER_account = float(total_num_likes / 12) + float(total_num_comments / 12)
        truncA = (ER_account / profile.followers)*100
        break
    i += 1
print(profile.get_profile_pic_url())
print(datapost)