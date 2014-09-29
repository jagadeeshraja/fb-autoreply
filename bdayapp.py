## R Jagadeesh, IIT Kanpur
## This is my version of the most common facebook reply app which help

import requests
import json


# Select a timeid so that you can reply only to those posts after that time point
AFTER = 1411065702

#Enter the token id of your facebook app you've created to reply
TOKEN = '<Your TOKEN>'

def Bday_posts():

    query = ("SELECT post_id, actor_id, message FROM stream WHERE "

            "filter_key = 'others' AND source_id = me() AND "

            "created_time > 1411065702 LIMIT 200")

    payload = {'q': query, 'access_token': TOKEN}

    r = requests.get('https://graph.facebook.com/fql', params=payload)

    result = json.loads(r.text)

    return result['data']


def Comment_thanks(wallposts):

    for wallpost in wallposts:


        r = requests.get('https://graph.facebook.com/%s' %

                wallpost['actor_id'])

        url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']

        user = json.loads(r.text)

        message = 'Thanks %s :)' % user['first_name']

        payload = {'access_token': TOKEN, 'message': message}

        s = requests.post(url, data=payload)


        print "Wall post %s done" % wallpost['post_id']


if __name__ == '__main__':

    Comment_thanks(Bday_posts())
