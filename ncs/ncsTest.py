import requests
import time
import random
import hashlib
# import uuid

prod=True

token='eyJhbGciOiJIUzUxMiJ9.eyJzZWxmT3BlcmF0ZWQiOjAsInN1YiI6IkNMRVJLIiwicm9sZSI6IlNVUEVSX1NFTExFUiIsIm5pY2tOYW1lIjoiYWxsZW4iLCJmb3VuZGVyIjpudWxsLCJyb2xlcyI6WyJCVVlFUiIsIlNFTExFUiIsIkNMRVJLIl0sInNlbGxlck5hbWUiOiLmtYvor5Xlupfpk7oiLCJjbGVya0lkIjo4LCJ1dWlkIjpudWxsLCJ1aWQiOjU2LCJzZWxsZXJJZCI6MTksImNsZXJrTmFtZSI6ImFsbGVuIiwiZXhwIjoxNTcxNjQ3ODE5LCJ1c2VybmFtZSI6ImFsbGVuIn0.VSjJmzcjJFL53uzjZ5nSYU9Rp1CZsqFjWRvH-cJ0XqKXEZfV6C_OtzErOFvlPQXR3YP-KRy1Xd9D8UWI0lrA_Q'
uid='56'
timestamp=str(int(time.time()*1000))
nonce=str(random.randint(100000,999999))
sign=hashlib.md5((uid+nonce+timestamp+token).encode("utf-8")).hexdigest()
#uuid=str(uuid.uuid4())
uuid ='708cd2f0-f3dd-11e9-9638-75ed5a371209'

print(timestamp+" "+nonce+" "+sign)

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
headers={'Authorization': token, 'uuid':uuid}
#url = 'http://localhost:7006/ncs/device/ncs_device_info/add'
#url = 'http://dev.seller.wdklian.com/seller/shops'
url='http://dev.seller.wdklian.com/seller/shops/createNextNewShop'

# 判断是否为生产环境
if prod:
  url+="?uid="+uid+"&timestamp="+timestamp+"&nonce="+nonce+"&sign="+sign

r=requests.post(url,data=postdata,headers=headers)
#r=requests.get(url,headers=headers)
print(r.text)