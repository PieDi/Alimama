#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy.spiders
from scrapy.http import  Request
from scrapy.selector import Selector
from ..spiders.transCookie import TransCookie

class AlimamaSpiders(scrapy.Spider):
    name = 'alimamaSpider'
    allowed_domains = ["alimama.com"]

    cookie = "t=e2a5dd8850b11d676d32dc138a823b6f; cna=8T7zEvjWTT4CAbSqatQmssYo; account-path-guide-s1=true; 28498392_yxjh-filter-1=true; cookie2=1f9cd71ace43742afd89aefcc3e9bee6; v=0; _tb_token_=e773ee437319; cookie32=d055d3dc2aee4e11f26891f4dd985a1b; cookie31=Mjg0OTgzOTIsJUU2JThEJUEyJUU0JUJEJUEwJUU4JThBJUIzJUU1JUJGJTgzJUU1JUE2JTgyJUU2JTk1JTg1LGFrODc1NTA5OTAzQHNpbmEuY29tLFRC; taokeisb2c=; taokeIsBoutiqueSeller=eQ%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTNfNikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcyLjAuMzYyNi4xMjEgU2FmYXJpLzUzNy4zNg%3D%3D; alimamapw=FXUgFSdwQXcCHCMDQXEPHHAlFXNSFSYGQXcOHCMHQXEBHHEnOQdXVFEEBQMBCQQFUwoKWlRWUwRV%0AA1ZQVQMHX1IBAFZa; JSESSIONID=A5FE4D49D08D1CBDF2EE438AA0410E5B; login=V32FPkk%2Fw0dUvg%3D%3D; rurl=aHR0cHM6Ly9wdWIuYWxpbWFtYS5jb20v; x5sec=7b22756e696f6e2d7075623b32223a22396162323639396365383237316138316231646433363638366630393731626643506546744f5146454c5842747558483276586553673d3d227d; l=bBamXXy7vzKtm43tBOfwquI8Y87tmQRfhsPzw4tMGIB19x1TcdUJ8Hwph67Wp3Q_E_5dsetydrtmAd3vJXz3Wt1..; isg=BAIC_j0Y6lDrC_BtLdZCWA_BUw6kewXvGHsqG0wZqXWqn6gZNGOZ_OAdS_tGz36F"
    trans = TransCookie(cookie)
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
        # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }
    # url中spm会变
    # a219t.7900221%2F1.1998910419.d07bd19c4.2a8f75a5ohGKuY
    # a219t.7900221%2F1.1998910419.d07bd19c4.2a8f75a58yLor5
    # sortType=9  表示销量从高到低
    def start_requests(self):
        # sortType = 9  按照销量排行
        urls = ["https://pub.alimama.com/promo/item/channel/index.htm?spm=a219t.7900221%2F1.1998910419.d07bd19c4.2a8f75a5ohGKuY&channel=nzjh&toPage=1&sortType=9&type=block"]
        for url in urls:
            yield Request(url=url, callback=self.parse)
    def parse(self, response):
        print("数据的返回是什么",response)
        # sel = Selector(response)
