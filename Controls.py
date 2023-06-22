"""This file contains the functions for testing """

import requests

url =  "http://192.168.0.20/cgi-bin/aw_ptz?cmd=&res=1"

myobj = {''}



splitURL = []

splitURL=url.split('=',1)

print (splitURL)

splitURL.insert(1,"=#PTS5050")

print (splitURL)

URL=''.join(splitURL)

print (URL)

x = requests.post(url)
print(x.text)

# Function take a value and pan the camera that value in degrees
def pan():
    x = requests.post(url)
    print(x.text)
