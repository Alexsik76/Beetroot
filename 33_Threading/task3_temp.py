import requests
import threading
import json


url = 'https://api.pushshift.io/reddit/comment/search/'
comments = []
search_param = '?fields=id,author'
url2 = 'https://api.pushshift.io/reddit/comment/search/'
param = '?author=Yurishirox&filter=author,id,body'
s = requests.get(url2+param)
s2 = s.json()
print(s2)
# print(s.text, type(s))

