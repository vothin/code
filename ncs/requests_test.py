#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: requests_test.py
    @time: 2019/10/29 15:54
    @desc:
'''
# ********************************************************


import requests
import time, random, hashlib

class Requests_Test():

    def __init__(self, uid, token, uuid):
        self.timestamp = str(int(time.time()) * 1000)
        self.nonce = str(random.randint(100000,999999))
        self.sign = hashlib.md5((uid + self.nonce + self.timestamp + token).encode('utf-8')).hexdigest()
        self.headers = {'Authorization': token, 'uuid': uuid}


    def get_requests(self, url, prod=False):
        if prod:
            url += "?uid=" + uid +"&timestamp=" + self.timestamp +"&nonce="+ self.nonce + "&sign=" + self.sign
        r = requests.get(url,headers=self.headers)
        print(r.text)


    def post_requests(self, url, postdata, prod=False):
        if prod:
            url += "?uid=" + uid +"&timestamp=" + self.timestamp +"&nonce="+ self.nonce + "&sign=" + self.sign
        r = requests.post(url, data=postdata, headers=self.headers)
        print(r.text)

if __name__ == '__main__':

    prod = True
    token='eyJhbGciOiJIUzUxMiJ9.eyJzZWxmT3BlcmF0ZWQiOjAsInN1YiI6IkNMRVJLIiwicm9sZSI6IlNVUEVSX1NFTExFUiIsIm5pY2tOYW1lIjoiYWxsZW4iLCJmb3VuZGVyIjpudWxsLCJyb2xlcyI6WyJCVVlFUiIsIlNFTExFUiIsIkNMRVJLIl0sInNlbGxlck5hbWUiOiLmtYvor5Xlupfpk7oiLCJjbGVya0lkIjo4LCJ1dWlkIjpudWxsLCJ1aWQiOjU2LCJzZWxsZXJJZCI6MTksImNsZXJrTmFtZSI6ImFsbGVuIiwiZXhwIjoxNTcxNjQ3ODE5LCJ1c2VybmFtZSI6ImFsbGVuIn0.VSjJmzcjJFL53uzjZ5nSYU9Rp1CZsqFjWRvH-cJ0XqKXEZfV6C_OtzErOFvlPQXR3YP-KRy1Xd9D8UWI0lrA_Q'
    uid='56'
    #uuid=str(uuid.uuid4())
    uuid ='708cd2f0-f3dd-11e9-9638-75ed5a371209'

    postdata={
      "address":"%E6%98%8E%E5%B9%B4",
      "town":"%E5%9F%8E%E5%8C%BA",
      "city":"%E5%AE%89%E5%BA%86%E5%B8%82",
      "county":"%E6%80%80%E5%AE%81%E5%8E%BF",
      "shopName":"%E5%98%BB%E5%98%BB%E5%98%BB",
      "cityId":"1140",
      "townId":"37586",
      "provinceId":"14",
      "province":"%E5%AE%89%E5%BE%BD",
      "countyId":"1145",
      "ancestorShopId":"124"
    }
    #url = 'http://localhost:7006/ncs/device/ncs_device_info/add'
    #url = 'http://dev.seller.wdklian.com/seller/shops'
    url='http://dev.seller.wdklian.com/seller/shops/createNextNewShop'

    r = Requests_Test(uid, token, uuid)
    r.get_requests(url, prod=True)
    # r.post_requests(url, postdata, prod=True)

