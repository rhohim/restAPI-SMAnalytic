# from flask import Flask, request, make_response, jsonify, Response
# from werkzeug.utils import secure_filename
# from flask_restful import Resource, Api 
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy 
# from functools import wraps
# from ast import literal_eval
# import json
# import jwt 
# import os 
# import datetime 
# from cryptography.fernet import Fernet
# import instaloader
# from datetime import date

# today = date.today()

# bot = instaloader.Instaloader()

# app = Flask(__name__)
# api = Api(app)

# CORS(app)


# #setting database
# filename = os.path.dirname(os.path.abspath(__file__))
# database = 'sqlite:///' + os.path.join(filename, 'db.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = database 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# app.config['SECRET_KEY'] = "cretivoxtechnology22"
# key = b'qXkOeccBROMqPi3MCFrNc6czJDrEJopBOpoWWYBKdpE='
# fernet = Fernet(key)

# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(50))
# #     password = db.Column(db.String(255))

# class Ig(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(255))
#     total_post = db.Column(db.Integer)
#     total_follower = db.Column(db.Integer)
#     total_following = db.Column(db.Integer)
#     evg_like = db.Column(db.Integer)
#     bio = db.Column(db.String(255))
#     link = db.Column(db.String(255))
#     url_img = db.Column(db.String(255))
#     er = db.Column(db.Integer)
#     post = db.Column(db.Text)
#     date = db.Column(db.Text)
    
#     # post =  db.Column(db.String(899))
#     # img_logo = db.Column(db.Text)
#     # name_logo = db.Column(db.Text)
#     # mimetype_logo = db.Column(db.Text)
    
# db.create_all()

# class insta(Resource):
#     def post(self):
#         d2 = today.strftime("%B %d, %Y")
#         profileid = request.form.get('username')
#         profile = instaloader.Profile.from_username(bot.context, profileid)
#         print("Username: ", profile.username)
#         print("User ID: ", profile.userid)
#         print("Number of Posts: ", profile.mediacount)
#         print("Followers Count: ", profile.followers)
#         print("Following Count: ", profile.followees)
#         print("Bio: ", profile.biography)
#         print("External URL: ", profile.external_url)   
#         print('\n')
#         num_followers = profile.followers
#         total_num_likes = 0
#         total_num_comments = 0
#         total_num_posts = 0
#         valueA , datapost= [], []
#         truncA = 0
#         i = 0

#         for post in profile.get_posts():
#             total_num_likes += post.likes
#             total_num_comments += post.comments
#             total_num_posts += 1
#             post = {
#                 "url_post": post.url,
#                 "like": post.likes,
#                 "comment": post.comments
#             }
#             datapost.append(post)
#             engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
#             valueA.append(engagement * 100)
            
#             if i == 11:
#                 ER_account = float(total_num_likes / 12) + float(total_num_comments / 12)
#                 truncA = (ER_account / profile.followers)*100
#                 break
#             i += 1
#         print("%.1f" % truncA)
        
#         con1 = Ig(username = profile.username,
#                   total_post = profile.mediacount,
#                   total_follower = profile.followers,
#                   total_following = profile.followees,
#                   bio = profile.biography,
#                   link = profile.external_url,
#                   er = "%.1f" % truncA,
#                   url_img = profile.get_profile_pic_url(),
#                   evg_like = "%.1f" % float(total_num_likes/total_num_posts), post = json.dumps(datapost),
#                   date = d2
#                   )

#         db.session.add(con1)

#         db.session.commit()
        
#         output = [{
#             "msg":"success",
#             "data" : {
#                 "Username" : profile.username,
#                 "Url_img" : profile.get_profile_pic_url(),
#                 "Number_of_Posts" : profile.mediacount,
#                 "Followers_Count" : profile.followers,
#                 "Following_Count" : profile.followees,
#                 "Bio" : profile.biography,
#                 "External_URL" : profile.external_url,
#                 "Evg_like" : "%.1f" % float(total_num_likes/total_num_posts),
#                 "ER" : "%.1f" % truncA,
#                 "post" : datapost,
#                 "date" : d2 
                
#             }
#         } 
#         ]
        
#         return make_response(jsonify(output), 200)

#     def get(self):
#         dataQuery = Ig.query.all()
#         # print(dataQuery[0].consumable)
#         output = [{
#             "id" : data.id,
#             "data" : {
#                 "Username" : data.username,
#                 "Url_img" : data.url_img,
#                 "Number_of_Posts" : data.total_post,
#                 "Followers_Count" : data.total_follower,
#                 "Following_Count" : data.total_following,
#                 "Bio" : data.bio,
#                 "External_URL" : data.link,
#                 "Evg_like" : data.evg_like,
#                 "ER" : data.er,
#                 "post" : literal_eval(data.post),
#                 "date" : data.date
                
                
#             }
#         } for data in dataQuery
#         ]
#         return make_response(jsonify(output), 200)
    
#     def delete(self):
#         db.session.query(Ig).delete()
#         db.session.commit()
        
#         return jsonify({"msg":"Deleted"})
        
    
# class instato2(Resource):

#     def get(self, id):
#         # print(data)
        
#         data = Ig.query.filter(Ig.id == id).first()
#         output = [{
#             "id" : data.id,
#             "data" : {
#                 "Username" : data.username,
#                 "url_img" : data.url_img,
#                 "Number_of_Posts " : data.total_post,
#                 "Followers_Count" : data.total_follower,
#                 "Following_Count" : data.total_following,
#                 "Bio" : data.bio,
#                 "External_URL" : data.link,
#                 "ER" : data.er,
#                 "post" : literal_eval(data.post),
#                 "date" : data.date
                
#             }
#         }
#         ]
#         return make_response(jsonify(output), 200)
    
#     def put(self,id):
#         d2 = today.strftime("%B %d, %Y")
#         dataUpdate = Ig.query.filter(Ig.id == id).first()
#         profileid = dataUpdate.username
#         profile = instaloader.Profile.from_username(bot.context, profileid)
#         num_followers = profile.followers
#         total_num_likes = 0
#         total_num_comments = 0
#         total_num_posts = 0
#         valueA,datapost = [],[]
#         truncA = 0
#         i = 0

#         for post in profile.get_posts():
#             total_num_likes += post.likes
#             total_num_comments += post.comments
#             total_num_posts += 1
#             post = {
#                 "url_post": post.url,
#                 "like": post.likes,
#                 "comment": post.comments
#             }
#             datapost.append(post)
#             engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
#             valueA.append(engagement * 100)
            
#             if i == 11:
#                 ER_account = float(total_num_likes / 12) + float(total_num_comments / 12)
#                 truncA = (ER_account / profile.followers)*100
#                 break
#             i += 1
#         dataUpdate.username = profile.username
#         dataUpdate.total_post = profile.mediacount
#         dataUpdate.total_follower = profile.followers
#         dataUpdate.total_following = profile.followees
#         dataUpdate.bio = profile.biography
#         dataUpdate.link = profile.external_url
#         dataUpdate.er = "%.1f" % truncA
#         dataUpdate.url_img = profile.get_profile_pic_url()
#         dataUpdate.evg_like = "%.1f" % float(total_num_likes/total_num_posts)
#         dataUpdate.date = d2
#         db.session.commit()
#         return make_response(jsonify({"msg":"updated"}), 200)
    
#     def delete(self, id):
#         own = Ig.query.filter(Ig.id == id).first()
#         db.session.delete(own)
#         db.session.commit()
        
#         return jsonify({"msg":"Deleted"})
        
   
# api.add_resource(insta, "/insta", methods=["POST","GET", "DELETE"])
# api.add_resource(instato2, "/insta/<id>", methods=["GET","PUT","DELETE"])

# if __name__ == "__main__":
#     app.run(debug=True,port=2023, host="0.0.0.0")

from flask import Flask, request, make_response, jsonify, Response
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from functools import wraps
from ast import literal_eval
import json
import jwt 
import os 
import datetime 
from cryptography.fernet import Fernet
import instaloader
from datetime import date


from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
from math import log, floor
from selenium.webdriver.common.by import By

def human_format(number):
    units = ['', 'K', 'M', 'G', 'T', 'P']
    k = 1000.0
    magnitude = int(floor(log(number, k)))
    return '%.2f%s' % (number / k**magnitude, units[magnitude])

def convert_str_to_number(x):
    total_stars = 0
    num_map = {'K':1000, 'M':1000000, 'B':1000000000}
    if x.isdigit():
        total_stars = int(x)
    else:
        if len(x) > 1:
            total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
    return int(total_stars)

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
    'Chrome/80.0.3987.132 Safari/537.36'
    


today = date.today()

bot = instaloader.Instaloader()

app = Flask(__name__)
api = Api(app)

CORS(app)


#setting database
filename = os.path.dirname(os.path.abspath(__file__))
database = 'sqlite:///' + os.path.join(filename, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "cretivoxtechnology22"
key = b'qXkOeccBROMqPi3MCFrNc6czJDrEJopBOpoWWYBKdpE='
fernet = Fernet(key)


class Tiktok(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    total_follower = db.Column(db.String(255))
    total_following = db.Column(db.String(255))
    share = db.Column(db.Integer)
    comment = db.Column(db.Integer)
    like = db.Column(db.Integer)
    view = db.Column(db.Integer)
    erview= db.Column(db.Integer)
    note = db.Column(db.Text)
    date = db.Column(db.String(255))
    tier = db.Column(db.String(255))
    img = db.Column(db.String(255))
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category", back_populates='tiktok')


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    color = db.Column(db.String(50))
    ig = db.relationship('Ig', back_populates="category")
    tiktok = db.relationship(Tiktok, back_populates = "category")

class Ig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    total_post = db.Column(db.Integer)
    total_follower = db.Column(db.Integer)
    total_following = db.Column(db.Integer)
    evg_like = db.Column(db.Integer)
    bio = db.Column(db.String(255))
    link = db.Column(db.String(255))
    url_img = db.Column(db.String(255))
    er = db.Column(db.Integer)
    # post = db.Column(db.Text)
    date = db.Column(db.Text)
    tier = db.Column(db.String(255))
    note = db.Column(db.Text)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category", back_populates='ig')
    
    # img = db.Column(db.Text)
    # name = db.Column(db.Text)
    # mimetype = db.Column(db.Text)
    
db.create_all()

class tiktok(Resource):
    def post(self):
        driver = webdriver.Chrome()
        driver.minimize_window()
        name = request.form.get('username')
        # data = {}
        driver.get("https://www.tiktok.com/@" + str(name))

        time.sleep(1)
        username = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/h1').text
        bio = driver.find_element(By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[1]/h2').text
        img_url = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[1]/span/img').get_attribute("src")
        scroll_pause_time = 1
        screen_height = driver.execute_script("return window.screen.height;")
        i = 1
        soup = BeautifulSoup(driver.page_source, "html.parser")
        follow = soup.find_all("div", {"class": "tiktok-1kd69nj-DivNumber"})
        following = follow[0].strong.text
        follower = follow[1].strong.text
        while True:
            # print(screen_height)
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
            i += 1
            time.sleep(scroll_pause_time)
            scroll_height = driver.execute_script("return document.body.scrollHeight;")  
            # if (screen_height) * i > scroll_height:
            #     break 
            videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})
            
            # print(type(videos))
            # print(len(videos))
            if len(videos) >= 29 :
            
                break
        total_like, total_comment, total_share = 0,0,0    
        intcom, intlike, intshare = 0,0,0  
        viewtik , datetik= [],[] 
        for i in range(len(videos)):
            print(i)
            # print(len(videos))
            strview = str(videos[i].strong.text)
            value = strview.find('K')
            value2 = strview.find('M')
            print(strview)
            if (value != -1) or (value2 != -1):
                if value != -1 :
                    strview = strview[:-1:]
                    print(strview , i, " " , value, " in minus")
                    intview = float(strview) * 1000
                elif value2 != -1 :
                    strview = strview[:-1:]
                    print(strview , i, " " , value, " in minus")
                    intview = float(strview) * 1000000
                        
            else:
                print(strview , i, " " , value, " positive")
                intview = int(strview)
            viewtik.append(int(intview))
            print(intview) #Total Views
            driver.get(videos[i].a["href"])
            like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[1]/strong').text
            comment = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[2]/strong').text
            share = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[3]/strong').text
            
            like1 = like.find('K')
            like2 = like.find('M')
            comment1 = comment.find('K')
            comment2 = comment.find('M')
            share1 = share.find('K')
            share2 = share.find('M')
            
            if (like1 != -1) or (like2 != -1):
                if like1 != -1 :
                    strview = like[:-1:]
                    print(strview , i, " " , like1, " in minus")
                    intlike = float(strview) * 1000
                elif like2 != -1 :
                    strview = like[:-1:]
                    print(strview , i, " " , like2, " in minus")
                    intlike = float(strview) * 1000000
            else:
                print(strview , i, " " , like, " positive")
                intview = int(like)
                    
            if (comment1 != -1) or (comment2 != -1):
                if comment1 != -1 :
                    strview = comment[:-1:]
                    print(strview , i, " " , comment1, " in minus")
                    intcom = float(strview) * 1000
                elif comment2 != -1 :
                    strview = comment[:-1:]
                    print(strview , i, " " , comment2, " in minus")
                    intcom = float(strview) * 1000000
            else:
                print(strview , i, " " , comment, " positive")
                intcom = int(comment)
                    
            if (share1 != -1) or (share2 != -1):
                if share1 != -1 :
                    strview = share[:-1:]
                    print(strview , i, " " , share1, " in minus")
                    intshare = float(strview) * 1000
                elif share2 != -1 :
                    strview = share[:-1:]
                    print(strview , i, " " , share2, " in minus")
                    intshare = float(strview) * 1000000
            else:
                print(strview , i, " " , share, " positive")
                if share == "Share" or share == "":
                    intshare = 0
                else:
                    intshare = int(share)
            
            print(intlike, " ", intcom, " ",intshare)        
            
            total_like += int(intlike)
            total_comment += int(intcom) 
            total_share += int(intshare)
        
        engview = (((total_like + total_comment + total_share)) /  np.sum(viewtik)) * 100 
        d2 = today.strftime("%B %d, %Y")
        tostr = convert_str_to_number(follower)
        if int(tostr) > 1000000:
            tier = "Mega"
        elif (int(tostr) > 500000) and (int(tostr) <= 1000000):
            tier = "Macro" 
        elif (int(tostr) > 50000) and (int(tostr) <= 500000):
            tier = "Mid-Tier" 
        elif (int(tostr) > 10000) and (int(tostr) <= 50000):
            tier = "Micro"
        else :
            tier = "Nano"
            
        print("View : " , human_format(np.sum(viewtik)))
        print("Follower : ", follower)
        print("Following : ",following)
        print("Like : " , total_like)
        print("comment : " , total_comment)
        print("share : " , total_share)
        print("username : " , username)
        print("bio : " , bio)

        output = [{
            "msg":"success",
            "data" : {
                "username" : username,
                "img" : img_url,
                "followers_Count" : follower,
                "following_Count" : following,
                "bio" : bio,
                "like" : total_like,
                "comment" : total_comment,
                "share" : total_share,
                "view" : human_format(np.sum(viewtik)),
                "er_view" : "%.1f" % engview,
                "tier" : tier,
                "date" : d2
                
            }
        } 
        ]
        
        return make_response(jsonify(output), 200)

    def get(self):
        dataQuery = Tiktok.query.all()
        output = [{
            "id" : data.id,
            "data" : {
                "username" : data.username,
                "img" : data.img,
                "followers_Count" : data.total_follower,
                "following_Count" : data.total_following,
                "bio" : data.bio,
                "like" : data.like,
                "comment" : data.comment,
                "share" : data.share,
                "view" : data.view,
                "er_view" : data.erview,
                "tier" : data.tier,
                "date" : data.date,
                "note" : data.note
                }
        } for data in dataQuery
        ]
        return make_response(jsonify(output), 200)
    
    def delete(self):
        db.session.query(Tiktok).delete()
        db.session.commit()
        
        return jsonify({"msg" : "Deleted"})    

class tiktokto2(Resource):
    def get(self, id):
        data = Tiktok.query.filter(Tiktok.id == id).first()
        output = [{
            "id" : data.id,
            "data" : {
                "username" : data.username,
                "img" : data.img,
                "followers_Count" : data.total_follower,
                "following_Count" : data.total_following,
                "bio" : data.bio,
                "like" : data.like,
                "comment" : data.comment,
                "share" : data.share,
                "view" : data.view,
                "er_view" : data.erview,
                "tier" : data.tier,
                "date" : data.date,
                "note" : data.note
                }
        }
        ]
        return make_response(jsonify(output), 200)
    def delete(self,id):
        own = Tiktok.query.filter(Tiktok.id == id).first()
        db.session.delete(own)
        db.session.commit()
    def put(self, id):
        dataUpdate = Tiktok.query.filter(Tiktok.id == id).first()
        name = dataUpdate.username
        driver = webdriver.Chrome()
        driver.minimize_window()
        name = request.form.get('username')
        # data = {}
        driver.get("https://www.tiktok.com/@" + str(name))
        cate = request.form.get('category')
        note = request.form.get('note')
        dbCategory = Category.query.all()
        queryCategory = [data.name for data in Category.query.all()]
        if cate in queryCategory:
            for i in range(len(dbCategory)):
                if dbCategory[i].name == cate:
                    idcategory = dbCategory[i].id
        else:
            return {"msg" : "there is no category"}
        time.sleep(1)
        username = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/h1').text
        bio = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[2]').text
        img_url = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[1]/span/img').get_attribute("src")
        scroll_pause_time = 1
        screen_height = driver.execute_script("return window.screen.height;")
        i = 1
        soup = BeautifulSoup(driver.page_source, "html.parser")
        follow = soup.find_all("div", {"class": "tiktok-1kd69nj-DivNumber"})
        following = follow[0].strong.text
        follower = follow[1].strong.text
        while True:
            # print(screen_height)
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
            i += 1
            time.sleep(scroll_pause_time)
            scroll_height = driver.execute_script("return document.body.scrollHeight;")  
            # if (screen_height) * i > scroll_height:
            #     break 
            videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})
            
            # print(type(videos))
            # print(len(videos))
            if len(videos) >= 29 :
            
                break
        total_like, total_comment, total_share = 0,0,0    
        intcom, intlike, intshare = 0,0,0  
        viewtik , datetik= [],[] 
        for i in range(len(videos)):
            print(i)
            # print(len(videos))
            strview = str(videos[i].strong.text)
            value = strview.find('K')
            value2 = strview.find('M')
            print(strview)
            if (value != -1) or (value2 != -1):
                if value != -1 :
                    strview = strview[:-1:]
                    print(strview , i, " " , value, " in minus")
                    intview = float(strview) * 1000
                elif value2 != -1 :
                    strview = strview[:-1:]
                    print(strview , i, " " , value, " in minus")
                    intview = float(strview) * 1000000
                        
            else:
                print(strview , i, " " , value, " positive")
                intview = int(strview)
            viewtik.append(int(intview))
            print(intview) #Total Views
            driver.get(videos[i].a["href"])
            like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[1]/strong').text
            comment = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[2]/strong').text
            share = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[3]/strong').text
            
            like1 = like.find('K')
            like2 = like.find('M')
            comment1 = comment.find('K')
            comment2 = comment.find('M')
            share1 = share.find('K')
            share2 = share.find('M')
            
            if (like1 != -1) or (like2 != -1):
                if like1 != -1 :
                    strview = like[:-1:]
                    print(strview , i, " " , like1, " in minus")
                    intlike = float(strview) * 1000
                elif like2 != -1 :
                    strview = like[:-1:]
                    print(strview , i, " " , like2, " in minus")
                    intlike = float(strview) * 1000000
            else:
                print(strview , i, " " , like, " positive")
                intview = int(like)
                    
            if (comment1 != -1) or (comment2 != -1):
                if comment1 != -1 :
                    strview = comment[:-1:]
                    print(strview , i, " " , comment1, " in minus")
                    intcom = float(strview) * 1000
                elif comment2 != -1 :
                    strview = comment[:-1:]
                    print(strview , i, " " , comment2, " in minus")
                    intcom = float(strview) * 1000000
            else:
                print(strview , i, " " , comment, " positive")
                intcom = int(comment)
                    
            if (share1 != -1) or (share2 != -1):
                if share1 != -1 :
                    strview = share[:-1:]
                    print(strview , i, " " , share1, " in minus")
                    intshare = float(strview) * 1000
                elif share2 != -1 :
                    strview = share[:-1:]
                    print(strview , i, " " , share2, " in minus")
                    intshare = float(strview) * 1000000
            else:
                print(strview , i, " " , share, " positive")
                if share == "Share" or share == "":
                    intshare = 0
                else:
                    intshare = int(share)
            
            print(intlike, " ", intcom, " ",intshare)        
            
            total_like += int(intlike)
            total_comment += int(intcom) 
            total_share += int(intshare)
        
        engview = (((total_like + total_comment + total_share)) /  np.sum(viewtik)) * 100 
        d2 = today.strftime("%B %d, %Y")
        tostr = convert_str_to_number(follower)
        if int(tostr) > 1000000:
            tier = "Mega"
        elif (int(tostr) > 500000) and (int(tostr) <= 1000000):
            tier = "Macro" 
        elif (int(tostr) > 50000) and (int(tostr) <= 500000):
            tier = "Mid-Tier" 
        elif (int(tostr) > 10000) and (int(tostr) <= 50000):
            tier = "Micro"
        else :
            tier = "Nano"
            
        dataUpdate.username = username
        dataUpdate.bio = bio
        dataUpdate.img = img_url
        dataUpdate.total_following = following
        dataUpdate.total_follower = follower
        dataUpdate.like = total_like
        dataUpdate.comment = total_comment
        dataUpdate.share = total_share
        dataUpdate.view = human_format(np.sum(viewtik))
        dataUpdate.erview = engview
        dataUpdate.tier = tier
        dataUpdate.date = d2
        dataUpdate.category_id = idcategory
        dataUpdate.note = note
        
        db.session.commit()
        return make_response(jsonify({"msg":"updated"}), 200)

class tiktokrel(Resource):
    def get(self):
        dataQuery = Tiktok.query.all()
        output = []
        for i in range(len(dataQuery)):
            val = {
                "id" : dataQuery[i].id,
                "data" : {
                    "username" : dataQuery[i].username,
                    "img" : dataQuery[i].img,
                    "followers_Count" : dataQuery[i].total_follower,
                    "following_Count" : dataQuery[i].total_following,
                    "bio" : dataQuery[i].bio,
                    "like" : dataQuery[i].like,
                    "comment" : dataQuery[i].comment,
                    "share" : dataQuery[i].share,
                    "view" : dataQuery[i].view,
                    "er_view" : dataQuery[i].erview,
                    "tier" : dataQuery[i].tier,
                    "date" : dataQuery[i].date,
                    "note" : dataQuery[i].note,
                    "category" : {
                        "id" : dataQuery[i].category.id,
                        "data" : {
                            "category" : dataQuery[i].category.name
                        }
                        
                    }
                }
            }
            output.append(val)
        return make_response(jsonify(output), 200)

class tiktokrelto(Resource):
    def get(self, id):
        data = Tiktok.query.filter(Tiktok.id == id).first()
        output = []
        val = {
            "id" : data.id,
            "data" : {
                "username" : data.username,
                "img" : data.img,
                "followers_Count" : data.total_follower,
                "following_Count" : data.total_following,
                "bio" : data.bio,
                "like" : data.like,
                "comment" : data.comment,
                "share" : data.share,
                "view" : data.view,
                "er_view" : data.erview,
                "tier" : data.tier,
                "date" : data.date,
                "note" : data.note,
                "category" : {
                    "id" : data.category.id,
                    "data" : {
                        "category" : data.category.name
                    }
                    
                }
            }
        }
        output.append(val)
        return make_response(jsonify(output), 200)

class Withcategorytiktok(Resource):
    def post(self):
        name = request.form.get('username')
        url_img = request.form.get('pic')
        follower = request.form.get('follower')
        following = request.form.get('following')
        bio = request.form.get('bio')
        er = request.form.get('er')
        like = request.form.get('like')
        comment = request.form.get("comment")
        share = request.form.get("share")
        view =request.form.get("view")
        date = request.form.get('date')
        tier = request.form.get('tier')
        cate = request.form.get('category')
        note = request.form.get('note')
        
        dbCategory = Category.query.all()
        queryCategory = [data.name for data in Category.query.all()]
        if cate in queryCategory:
            for i in range(len(dbCategory)):
                if dbCategory[i].name == cate:
                    idcategory = dbCategory[i].id
        else:
            return {"msg" : "there is no category"}
        
        con1 = Tiktok(
            username = name,
            bio = bio,
            total_follower = follower,
            total_following = following,
            share = share,
            view = view,
            like = like,
            comment = comment,
            erview = er,
            date = date,
            tier = tier ,
            img = url_img,
            category_id = idcategory,
            note = note
            
            
        )

        db.session.add(con1)

        db.session.commit()
        return make_response({"msg" : "success"}, 200)

class withcategory(Resource):
    def post(self):
        name = request.form.get('username')
        post = request.form.get('post')
        follower = request.form.get('follower')
        following = request.form.get('following')
        bio = request.form.get('bio')
        link = request.form.get('link')
        er = request.form.get('er')
        like = request.form.get('like')
        date = request.form.get('date')
        tier = request.form.get('tier')
        cate = request.form.get('category')
        url = request.form.get('pic')
        note = request.form.get('note')
        # pic = request.files['pic']
        # if not pic :
        #     return jsonify({"msg" : "picture not allowed"})
        # filename = secure_filename(pic.filename)
        # mimetype = pic.mimetype
        # if not filename or not mimetype:
        #     return jsonify({"msg":"bad upload"})
        
        # dataIg = Ig.query.filter(Ig.username == name).first()
        print(url)
        dbCategory = Category.query.all()
        queryCategory = [data.name for data in Category.query.all()]
        if cate in queryCategory:
            for i in range(len(dbCategory)):
                if dbCategory[i].name == cate:
                    idcategory = dbCategory[i].id
        else:
            return {"msg" : "there is no category"}
        # dataIg.category_id = idcategory
        
        con1 = Ig(username = name,
                  total_post = post,
                  total_follower = follower,
                  total_following = following,
                  bio = bio,
                  link = link,
                  er = er,
                  url_img = url,
                  evg_like = like,
                  date = date,
                  tier = tier,
                  note = note,
                  category_id = idcategory,
                #   img = pic.read(),
                #   name = filename,
                #   mimetype = mimetype
        
                  )

        db.session.add(con1)
    
        db.session.commit()
        return make_response({"msg" : "success"}, 200)

# class GetImgInsta(Resource):
#     def get(self, id):
#         print(id)
#         img = Ig.query.filter(Ig.id == id).first()
#         # print(img.img)
#         if not img:
#            return jsonify({"msg":"bad request"}) 
#         return Response(img.img, mimetype=img.mimetype)        
        

class insta(Resource):
    def post(self):
        d2 = today.strftime("%B %d, %Y")
        profileid = request.form.get('username')
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
        valueA , datapost= [], []
        truncA = 0
        i = 0
        if int(profile.followers) > 1000000:
            tier = "Mega"
        elif (int(profile.followers) > 500000) and (int(profile.followers) <= 1000000):
            tier = "Macro" 
        elif (int(profile.followers) > 50000) and (int(profile.followers) <= 500000):
            tier = "Mid-Tier" 
        elif (int(profile.followers) > 10000) and (int(profile.followers) <= 50000):
            tier = "Micro"
        else :
            tier = "Nano"
        for post in profile.get_posts():
            total_num_likes += post.likes
            total_num_comments += post.comments
            total_num_posts += 1
            # post = {
            #     "url_post": post.url,
            #     "like": post.likes,
            #     "comment": post.comments
            # }
            # datapost.append(post)
            engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
            valueA.append(engagement * 100)
            
            if i == 11:
                ER_account = float(total_num_likes / 12) + float(total_num_comments / 12)
                truncA = (ER_account / profile.followers)*100
                break
            i += 1
        print("%.1f" % truncA)
        
        # con1 = Ig(username = profile.username,
        #           total_post = profile.mediacount,
        #           total_follower = profile.followers,
        #           total_following = profile.followees,
        #           bio = profile.biography,
        #           link = profile.external_url,
        #           er = "%.1f" % truncA,
        #           url_img = profile.get_profile_pic_url(),
        #           evg_like = "%.1f" % float(total_num_likes/total_num_posts),
        #           date = d2,tier =tier
        
        #           )

        # db.session.add(con1)

        # db.session.commit()
        
        output = [{
            "msg":"success",
            "data" : {
                "Username" : profile.username,
                "Url_img" : profile.get_profile_pic_url(),
                "Number_of_Posts" : profile.mediacount,
                "Followers_Count" : profile.followers,
                "Following_Count" : profile.followees,
                "Bio" : profile.biography,
                "External_URL" : profile.external_url,
                "Evg_like" : "%.1f" % float(total_num_likes/total_num_posts),
                "ER" : "%.1f" % truncA,
                "Tier" : tier,
                "Date" : d2 
                
            }
        } 
        ]
        
        return make_response(jsonify(output), 200)

    def get(self):
        dataQuery = Ig.query.all()
        # print(dataQuery[0].category.id)
        output = []
        for i in range(len(dataQuery)):
            val = {
                "id" : dataQuery[i].id,
                "data" : {
                    "Username" : dataQuery[i].username,
                    "Url_img" : dataQuery[i].url_img,
                    "Number_of_Posts" : dataQuery[i].total_post,
                    "Followers_Count" : dataQuery[i].total_follower,
                    "Following_Count" : dataQuery[i].total_following,
                    "Bio" : dataQuery[i].bio,
                    "External_URL" : dataQuery[i].link,
                    "Evg_like" : dataQuery[i].evg_like,
                    "ER" : dataQuery[i].er,
                    # "post" : literal_eval(dataQuery[i].post),
                    "date" : dataQuery[i].date,
                    "tier" : dataQuery[i].tier,
                    "note" : dataQuery[i].note,
                    # "category" : {
                    #     "id" : dataQuery[i].category.id,
                    #     "data" : {
                    #         "category" : dataQuery[i].category.name
                    #     }
                        
                    # }
                }
            }
            output.append(val)
        return make_response(jsonify(output), 200)
    
    def delete(self):
        db.session.query(Ig).delete()
        db.session.commit()
        
        return jsonify({"msg":"Deleted"})
        
    
class instato2(Resource):

    def get(self, id):
        # print(data)
        
        data = Ig.query.filter(Ig.id == id).first()
        output = [{
            "id" : data.id,
            "data" : {
                "Username" : data.username,
                "url_img" : data.url_img,
                "Number_of_Posts " : data.total_post,
                "Followers_Count" : data.total_follower,
                "Following_Count" : data.total_following,
                "Bio" : data.bio,
                "External_URL" : data.link,
                "ER" : data.er,
                # "post" : literal_eval(data.post),
                "Date" : data.date,
                "Note" : data.note,
                "Tier" : data.tier
                
            }
        }
        ]
        return make_response(jsonify(output), 200)
    
    def put(self,id): #########################
        d2 = today.strftime("%B %d, %Y")
        dataUpdate = Ig.query.filter(Ig.id == id).first()
        profileid = dataUpdate.username
        profile = instaloader.Profile.from_username(bot.context, profileid)
        num_followers = profile.followers
        total_num_likes = 0
        total_num_comments = 0
        total_num_posts = 0
        valueA,datapost = [],[]
        truncA = 0
        i = 0
        cate = request.form.get('category')
        note = request.form.get('note')
        print(cate)
        dbCategory = Category.query.all()
        queryCategory = [data.name for data in Category.query.all()]
        if cate in queryCategory:
            for i in range(len(dbCategory)):
                if dbCategory[i].name == cate:
                    idcategory = dbCategory[i].id
        else:
            return {"msg" : "there is no category"}
        
        if int(profile.followers) > 1000000:
            tier = "Mega"
        elif (int(profile.followers) > 500000) and (int(profile.followers) <= 1000000):
            tier = "Macro" 
        elif (int(profile.followers) > 50000) and (int(profile.followers) <= 500000):
            tier = "Mid-Tier" 
        elif (int(profile.followers) > 10000) and (int(profile.followers) <= 50000):
            tier = "Micro"
        else :
            tier = "Nano"
        
        for post in profile.get_posts():
            total_num_likes += post.likes
            total_num_comments += post.comments
            total_num_posts += 1
            # post = {
            #     "url_post": post.url,
            #     "like": post.likes,
            #     "comment": post.comments
            # }
            # datapost.append(post)
            engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
            valueA.append(engagement * 100)
            
            if i == 11:
                ER_account = float(total_num_likes / 12) + float(total_num_comments / 12)
                truncA = (ER_account / profile.followers)*100
                break
            i += 1
        dataUpdate.username = profile.username
        dataUpdate.total_post = profile.mediacount
        dataUpdate.total_follower = profile.followers
        dataUpdate.total_following = profile.followees
        dataUpdate.bio = profile.biography
        dataUpdate.link = profile.external_url
        dataUpdate.er = "%.1f" % truncA
        dataUpdate.url_img = profile.get_profile_pic_url()
        dataUpdate.evg_like = "%.1f" % float(total_num_likes/total_num_posts)
        dataUpdate.date = d2
        dataUpdate.tier = tier
        dataUpdate.note = note
        dataUpdate.category_id = idcategory
        
        
        db.session.commit()
        return make_response(jsonify({"msg":"updated"}), 200)
    
    def delete(self, id):
        own = Ig.query.filter(Ig.id == id).first()
        db.session.delete(own)
        db.session.commit()
        
        return jsonify({"msg":"Deleted"})
        
class instarel(Resource):
    def get(self):
        dataQuery = Ig.query.all()
        # print(dataQuery[0].category.id)
        output = []
        for i in range(len(dataQuery)):
            val = {
                "id" : dataQuery[i].id,
                "data" : {
                    "Username" : dataQuery[i].username,
                    "Url_img" : dataQuery[i].url_img,
                    "Number_of_Posts" : dataQuery[i].total_post,
                    "Followers_Count" : dataQuery[i].total_follower,
                    "Following_Count" : dataQuery[i].total_following,
                    "Bio" : dataQuery[i].bio,
                    "External_URL" : dataQuery[i].link,
                    "Evg_like" : dataQuery[i].evg_like,
                    "ER" : dataQuery[i].er,
                    # "post" : literal_eval(dataQuery[i].post),
                    "date" : dataQuery[i].date,
                    "tier" : dataQuery[i].tier,
                    "note" : dataQuery[i].note,
                    "category" : {
                        "id" : dataQuery[i].category.id,
                        "data" : {
                            "category" : dataQuery[i].category.name,
                            "color" :dataQuery[i].category.color
                        }
                        
                    }
                }
            }
            output.append(val)
        return make_response(jsonify(output), 200)

class instarelto(Resource):
    def get(self, id):
        data = Ig.query.filter(Ig.id == id).first()
        output = []
        val = {
            "id" : data.id,
            "data" : {
                "Username" : data.username,
                "Url_img" : data.url_img,
                "Number_of_Posts" : data.total_post,
                "Followers_Count" : data.total_follower,
                "Following_Count" : data.total_following,
                "Bio" : data.bio,
                "External_URL" : data.link,
                "Evg_like" : data.evg_like,
                "ER" : data.er,
                # "post" : literal_eval(data.post),
                "date" : data.date,
                "tier" : data.tier,
                "category" : {
                    "id" : data.category.id,
                    "data" : {
                        "category" : data.category.name,
                        "color" :data.category.color
                    }
                    
                }
            }
        }
        output.append(val)
        return make_response(jsonify(output), 200)
        

class category(Resource):
    def post(self):
        category = request.form.get('category')
        color = request.form.get('color')
        con = Category(name = category,color=color)
        db.session.add(con)
        db.session.commit()
        return make_response({"msg" : "success"}, 200)
        
    def get(self):
        dataQuery = Category.query.all()
        output = [{
            "id" : data.id,
            "data" : {
                "name" : data.name,
                "color" : data.color
            }
        } for data in dataQuery
        ]
        # print(dataQuery[1].ig[0].username)
        return make_response(jsonify(output), 200)
    
    def delete(self):
        db.session.query(Category).delete()
        db.session.commit()
        
        return jsonify({"msg":"Deleted"})
    
class catto2(Resource):
    def delete(self, id):
        own = Category.query.filter(Category.id == id).first()
        db.session.delete(own)
        db.session.commit()
        
        return jsonify({"msg":"Deleted"})
    
    def put(self,id):
        own = Category.query.filter(Category.id == id).first()
        data = request.form.get('category')
        own.name = data
        db.session.commit()
        return make_response({"msg" : "success"}, 200)
        
        
    
class categoryall(Resource):
    def get(self):
        dataQuery = Category.query.all()
        output= []
        for i in range(len(dataQuery)):
            print(len(dataQuery[i].ig))
            outig,outtik = [], []
            for x in range(len(dataQuery[i].ig)):
                dataig = {
                        "id" : dataQuery[i].ig[x].id,
                        "data" : {
                            "Username" : dataQuery[i].ig[x].username,
                            "Url_img" : dataQuery[i].ig[x].url_img,
                            "Number_of_Posts" : dataQuery[i].ig[x].total_post,
                            "Followers_Count" : dataQuery[i].ig[x].total_follower,
                            "Following_Count" : dataQuery[i].ig[x].total_following,
                            "Bio" : dataQuery[i].ig[x].bio,
                            "External_URL" : dataQuery[i].ig[x].link,
                            "Evg_like" : dataQuery[i].ig[x].evg_like,
                            "ER" : dataQuery[i].ig[x].er,
                            "date" : dataQuery[i].ig[x].date,
                            "tier" : dataQuery[i].ig[x].tier,
                            "note" : dataQuery[i].ig[x].note
                        }
                }
                outig.append(dataig)
            
            for x in range(len(dataQuery[i].tiktok)):
                datatiktok = {
                        "id" : dataQuery[i].tiktok[x].id,
                        "data" : {
                            "username" : dataQuery[i].tiktok[x].username,
                            "img" : dataQuery[i].tiktok[x].img,
                            "followers_Count" : dataQuery[i].tiktok[x].total_follower,
                            "following_Count" : dataQuery[i].tiktok[x].total_following,
                            "bio" : dataQuery[i].tiktok[x].bio,
                            "like" : dataQuery[i].tiktok[x].like,
                            "comment" : dataQuery[i].tiktok[x].comment,
                            "share" : dataQuery[i].tiktok[x].share,
                            "view" : dataQuery[i].tiktok[x].view,
                            "er_view" : dataQuery[i].tiktok[x].erview,
                            "tier" : dataQuery[i].tiktok[x].tier,
                            "date" : dataQuery[i].tiktok[x].date,
                            "note" : dataQuery[i].tiktok[x].note
                        }
                }
                outtik.append(datatiktok)    
                
            datacat = {
                "id" : dataQuery[i].id,
                "name" : dataQuery[i].name,
                "data" : {
                    "instagram" : outig,
                    "tiktok" : outtik
                    }
                }
            output.append(datacat)
        return make_response(jsonify(output), 200)
    
class categoryallid(Resource):
    def get(self, id):
        data = Category.query.filter(Category.id == id).first()
        output,outtik = [], []
        print(data.ig)
        for i in range(len(data.ig)):
            dataig = {
                "id" : data.ig[i].id,
                "data" : {
                            "Username" : data.ig[i].username,
                            "Url_img" : data.ig[i].url_img,
                            "Number_of_Posts" : data.ig[i].total_post,
                            "Followers_Count" : data.ig[i].total_follower,
                            "Following_Count" : data.ig[i].total_following,
                            "Bio" : data.ig[i].bio,
                            "External_URL" : data.ig[i].link,
                            "Evg_like" : data.ig[i].evg_like,
                            "ER" : data.ig[i].er,
                            "date" : data.ig[i].date,
                            "tier" : data.ig[i].tier,
                            "note" : data.ig[i].note
                        }
            }
            output.append(dataig)
        
        for i in range(len(data.tiktok)):
            datatik = {
                "id" : data.tiktok[i].id,
                "data" : {
                            "username" : data.tiktok[i].username,
                            "img" : data.tiktok[i].img,
                            "followers_Count" : data.tiktok[i].total_follower,
                            "following_Count" : data.tiktok[i].total_following,
                            "bio" : data.tiktok[i].bio,
                            "like" : data.tiktok[i].like,
                            "comment" : data.tiktok[i].comment,
                            "share" : data.tiktok[i].share,
                            "view" : data.tiktok[i].view,
                            "er_view" : data.tiktok[i].erview,
                            "tier" : data.tiktok[i].tier,
                            "date" : data.tiktok[i].date,
                            "note" : data.tiktok[i].note
                        }
            }
            outtik.append(datatik)
        outcat = [{
            "id" : data.id,
            "name" : data.name,
            "color" : data.color,
            "data" : {
                "instagram" : output,
                "tiktok" : outtik
            }
        }]
        return make_response(jsonify(outcat), 200)
        
   
api.add_resource(insta, "/insta", methods=["POST","GET", "DELETE"])
api.add_resource(instato2, "/insta/<id>", methods=["GET","PUT","DELETE"])

api.add_resource(instarel, "/insta/populate", methods=["GET"])
api.add_resource(instarelto, "/insta/populate/<id>", methods=["GET"])

api.add_resource(category, "/insta/category", methods=["POST","GET","DELETE"])
api.add_resource(catto2, "/insta/category/<id>" , methods=["PUT","DELETE"])

api.add_resource(categoryall, "/insta/category/populate", methods=["GET"])
api.add_resource(categoryallid, "/insta/category/populate/<id>", methods=["GET"])

api.add_resource(withcategory, "/insta/push", methods=["POST","GET"])
# api.add_resource(GetImgInsta, "/insta/picture/<id>", methods=["GET"])

api.add_resource(Withcategorytiktok, "/tiktok/push", methods=["POST","GET"])

api.add_resource(tiktok, "/tiktok", methods=["POST", "GET", "DELETE"])
api.add_resource(tiktokto2, "/tiktok/<id>", methods=["GET" , "DELETE", "PUT"])

api.add_resource(tiktokrel, "/tiktok/populate", methods=["GET"])
api.add_resource(tiktokrelto, "/tiktok/populate/<id>", methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True,port=2023, host="0.0.0.0")

