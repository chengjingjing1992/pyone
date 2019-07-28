#coding=utf-8
import requests
url="http://servemobiletest.kuaishouax.com/ApiProduct/GetProductByCondition"

data={
    "condition":"{'page':{'pagesize':20,'pageindex':1},'sort':{'orderby':0,'desc':0}}"
}


r=requests.post(url,data=data)
print(r.text)

