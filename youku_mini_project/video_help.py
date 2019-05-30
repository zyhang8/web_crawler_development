# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 12:34
# @Author  : zyh
# @File    : video_help.py
# @Software: PyCharm

import re
import urllib.request
import json
import time
import random
import sys


# url:https://v.youku.com/v_show/id_XMzA1Mjk3NTYyOA==.html?sharefrom=iphone&sharekey=4b77e9cd73db40b940a4eeec772752ea3
def getVideoInfo(url):
    ruleTitle = re.compile('<title>(.*)</title>')
    ruleId = re.compile('http://v.youku.com/v_show/id_(.*).html')
    videoTitle = ruleTitle.findall(urllib.request.urlopen(url).read().decode('utf8'))
    videoId = ruleId.findall(url)
    return videoTitle[0], videoId[0]


def getTrueLink(videoid):
    data = urllib.request.urlopen('http://v.youku.com/player/getPlayList/VideoIDS/' + videoid)
    info = json.loads(data.read().decode('utf8'))

    segs = info['data'][0]['segs']
    types = segs.keys()

    seed = info['data'][0]['seed']
    source = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/\\:._-1234567890")
    mixed = ''
    while source:
        seed = (seed * 211 + 30031) & 0xFFFF
        index = seed * len(source) >> 16
        c = source.pop(index)
        mixed += c

    ids = info['data'][0]['streamfileids']['flv'].split('*')[:-1]
    vid = ''.join(mixed[int(i)] for i in ids)

    sid = '%s%s%s' % (int(time.time() * 1000), random.randint(1000, 1999), random.randint(1000, 9999))

    urls = []
    for s in segs['flv']:
        no = '%02x' % int(s['no'])
        url = 'http://f.youku.com/player/getFlvPath/sid/%s_%s/st/flv/fileid/%s%s%s?K=%s&ts=%s' % (
        sid, no, vid[:8], no.upper(), vid[10:], s['k'], s['seconds'])
        urls.append(url)
    return urls


def down2file(urls, filename):
    f = open(filename, 'wb')
    fileNum = len(urls)
    count = 0
    for url in urls:
        count += 1
        print('downloading file %d/%d' % (count, fileNum))
        req = urllib.request.Request(url, headers={'Referer': 'http://www.youku.com'})
        data = urllib.request.urlopen(req).read()
        f.write(data)
    f.close()
    print('download ' + filename + ' OK!')


def youkuDown(link):
    print("A")
    videotitle, videoid = getVideoInfo(link)
    urls = getTrueLink(videoid)
    down2file(urls, videotitle + '.flv')


if __name__ == '__main__':
    youkuDown("http://v.youku.com/v_show/id_XMzA1Mjk3NTYyOA.html")
