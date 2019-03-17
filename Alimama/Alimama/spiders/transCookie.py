# -*- coding: utf-8 -*-
import sys

class TransCookie(object):
    def __init__(self, cookie):
        print('-------', cookie)
        self.cookie = cookie
    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict
