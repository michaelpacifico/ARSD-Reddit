
from urllib import request
from flask import Flask, request, redirect
from flask import render_template, url_for
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from gevent import reinit

# auth imports
import random
import socket
import sys
import praw, requests, json


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)

#@app.route('/')
#def home():
#    return render_template('home.html')


def get_act():
    timevec = []
    

    #User Pattern of Use Data
    reddit = praw.Reddit(client_id = 'gNfPOVg0wvJNvWpjHmPieQ',
    client_secret = 'QLNy6wg2d_d3Wpr-ezFWdq-RhyZK4w',
    username = 'Solid-Guidance1826', password = '1234567890@', user_agent = 'prawtesting')

    n = 0
    newday = 0

    #print('Posted Comments:')
    for comment in reddit.user.me().comments.new(limit=None): 
        time = comment.created_utc 
        day = int(time/86400)
        c = timevec.count(day)
        if c == 0:
            timevec.append(day)
            newday += 1
        n+= 1
    #print( comment.body.split("\n", 1)[0][:79])
    #print(str(datetime.fromtimestamp(time)))

    #print(newday, n)
    #print("\n")
        
    #print('Posted Subreddits:')  
    for subm in reddit.user.me().submissions.new(limit=None):
        time = subm.created_utc
        day = int(time/86400)
        c = timevec.count(day)
        if c == 0:
            timevec.append(day)
            newday += 1
        n+= 1 
        #print(subm.title.split("\n", 1)[0][:79])
        #print(str(datetime.fromtimestamp(time)))
        #print(time)

    #print(newday, n)
    #print("\n")

    #print('Upvoted Subreddits:')   
    for subupvote in reddit.user.me().upvoted(limit=None):
        time = subupvote.created_utc
        day = int(time/86400)
        c = timevec.count(day)
        if c == 0:
            timevec.append(day)
            newday += 1
        n += 1
        #print(subupvote.title.split("\n", 1)[0][:79])
        #print(str(datetime.fromtimestamp(time)))
        #print(time)

    #print(newday, n)
    #print("\n")

    #print('Downvoted Subreddits:')
    for subdownvote in reddit.user.me().downvoted(limit=None):
        time = subdownvote.created_utc
        day = int(time/86400)
        c = timevec.count(day)
        if c == 0:
            timevec.append(day)
            newday += 1
        n+= 1
        #print(subdownvote.title.split("\n", 1)[0][:79])
        #print(str(datetime.fromtimestamp(time)))
        #print(time)

    #print(newday, n) #newday = active days n = total number of activities of any kind
    #print("\n")

    minday = min(timevec)
    maxday = max(timevec)
    total = maxday - minday

    #print('Days since first on reddit: ', total) #total time anythings happened 

    numweeks = total/7
    daysact = newday/numweeks
    #print('number of days per week active: ', daysact) #number of days per week active

    postact = n/newday
    #print('Activities per active day: ', postact) # number of activities (comments, subreddits, etc...) per active day

    #print(timevec)
    return total, daysact, postact

@app.route("/activity")
def act():
    total, daysact, postact = get_act()
    return render_template("activity.html", total = total, daysact = daysact, postact = postact)

if __name__ == '__main__':
    app.run()