import requests
import time
import random
import hashlib
import uuid
import json

prod=True


#uuid=str(uuid.uuid4())
uuid ='708cd2f0-f3dd-11e9-9638'

# login
login_data = {
  "username":"13412345678",
  "password":hashlib.md5("123456".encode("utf-8")).hexdigest()
}
login_result = requests.get(
  url="http://dev.buyer.wdklian.com/passport/login/noCaptcha",
  params=login_data,
  headers={"uuid":uuid}
)
#print(login_result.text)
json_data = json.loads(login_result.text)
token = json_data['access_token']


uid='2247'
timestamp=str(int(time.time()*1000))
nonce=str(random.randint(100000,999999))
sign1 = uid+nonce+timestamp+token
sign=hashlib.md5((uid+nonce+timestamp+token).encode("utf-8")).hexdigest()


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
postdata={
  "goods_id":"345"
}
headers={'Authorization': token, 'uuid':uuid}
#url = 'http://localhost:7006/ncs/device/ncs_device_info/add'
#url = 'http://dev.buyer.wdklian.com/members'
url='http://dev.buyer.wdklian.com/members/collection/goods'

if prod:
  url+="?uid="+uid+"&timestamp="+timestamp+"&nonce="+nonce+"&sign="+sign

r=requests.post(url,data=postdata,headers=headers)
#r=requests.get(url,headers=headers)
print(r.text)