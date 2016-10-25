from bs4 import BeautifulSoup
import praw
import requests
import subprocess
import re
import os
l=[]
def get_submission(submission):
    for x in submission:
        if x.over_18 == False and x not in l:
            l.append(x.url)
            return x.url

r = praw.Reddit(user_agent='my_cool_application')
submission = r.get_subreddit('minimalwallpaper').get_top_from_day(limit=1)
imageurl = get_submission(submission)
response = requests.get(imageurl)
soup = BeautifulSoup(response.text, 'html.parser')
azoom = soup.findAll('a',{'class':'zoom'})
iurl = azoom[0].get('href')
iurlext = iurl[::-1][:iurl.index('.')+1][::-1]
print 'http://i.'+imageurl[7:]+iurlext
response1 = requests.get('http://i.'+imageurl[7:]+iurlext)
print response1.status_code
"""count=2
while (response.status_code != 200):
    submission = r.get_subreddit('minimalwallpaper').get_top(limit=2)
    imageurl = get_submission(submission) + '.jpg'
    if (response.status_code != 200):
        print("Error")
        count+=1"""
path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','Resources')
fo = open(path + '/wallpaper.jpg', 'wb')
for chunk in response1.iter_content(4096):
    fo.write(chunk)
fo.close()

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to alias POSIX file "%s"
end tell
END"""

def set_desktop_background(filename):
    subprocess.Popen(SCRIPT%filename, shell=True)
    
set_desktop_background(path + '/wallpaper.jpg')
