#coding=utf-8
import requests
# 组装请求
url="http://servemobiletest.kuaishouax.com/ApiAjax/LimitedTimeSpikeList"

params={
    "type":"5"
}
# 发送请求获取结果
r=requests.request("post",url,params=params)
print(r.text)

#结果解析
