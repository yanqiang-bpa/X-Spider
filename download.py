#coding=utf-8
import urllib2
import urllib
import re
import json

def getHtml():

    req = urllib2.Request("http://www.ximalaya.com/2452186/album/3230275")
    req.add_header("User-Agent", "Mozilla/5.0")
    source = urllib2.urlopen(req)
    html =  source.read()
    reg = r'sound_ids=\"(.+?)\">'
    sound_ids_reg = re.compile(reg)
    sound_ids_str = re.findall(sound_ids_reg, html)[0]
    sound_ids = sound_ids_str.split(",")

    sound_id_0 = sound_ids[0]

    for sound_id in sound_ids:

        print "http://www.ximalaya.com/tracks/" + sound_id + ".json"

        trackRes = urllib2.Request("http://www.ximalaya.com/tracks/" + sound_id + ".json")
        trackRes.add_header("User-Agent", "Mozilla/5.0")
        source = urllib2.urlopen(trackRes)
        html =  source.read()
        jsonData = json.loads(html)
        soundPath = jsonData["play_path"]
        soundTitle = jsonData["title"]
        soundPublishDate = jsonData["formatted_created_at"]
        print soundPath
        print soundTitle
        print soundPublishDate

        testfile = urllib.URLopener()

        testfile.retrieve(soundPath, soundTitle + str(".m4a"))


getHtml()
