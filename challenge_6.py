#!/usr/bin/python
# Python challenge #1: http://www.pythonchallenge.com/pc/def/map.html
# challenge: http://www.pythonchallenge.com/pc/def/channel.html
# Solution: http://www.pythonchallenge.com/pcc/def/oxygen.html
import sys
from sys import stdin
import re ## RexExp
import os
import json
import time
import subprocess
import string
#import urllib
#import urllib2
import pickle
import zipfile
from zipfile import ZipFile
#from StringIO import StringIO
import requests
import io

# Getting zip file automatically

zip_url = "http://www.pythonchallenge.com/pc/def/channel.zip"

#zip_loc = "/mnt/c/Users/arturo/OneDrive/NEW_LIFE/Python/Python Challenge/files/channel.zip"
readme_name = "readme.txt"
reqResponse = requests.get(zip_url)

nothing = "90052"
prev_nothing = ""
pattern = re.compile("Next nothing is ")
comments = []
pairs = []
while True:
    with ZipFile(io.BytesIO(reqResponse.content)) as zipFile:
        fileName = nothing + ".txt"
        myFile = zipFile.open(fileName)
        filecontent = myFile.read().decode()
        comment = zipFile.getinfo(fileName).comment.decode()
        comments.append(comment)
        if pattern.search(filecontent):
            #pass
            nothing = pattern.split(filecontent)[1]
        else:
            #print ("From",prev_nothing,"to",nothing,":",filecontent,sep=' ')
	    #print 'From {0} to {1} : {2}'.format(prev_nothing,nothing,filecontent)
            #print(''.join(comments))
            print ''.join(comments)
            sys.exit(0)
