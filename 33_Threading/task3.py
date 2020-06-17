# Requests using multiprocessing
import requests
import threading
# import json

url = "https://api.pushshift.io/reddit/comment/search/"
comments = []
# authors = ["Yurishirox", "Zeewitje", "Magic-Prankster"]
authors = ["Yurishirox"]
key_list = ['id', 'author', 'body']


def read_from_API(url: str, param: str):
    reqest = requests.get(f'{url}{param}')
    thead = {'thead': threading.current_thread().getName()}
    data_to_add = reqest.json()['data']
    data1 = list(map(lambda x: x.update(thead), data_to_add))
    # map(lambda x: x.update(thead), data_to_add)
    return data1


for author in authors:
    param = f'?author={author}&filter=author,id,body'
    comments.append(read_from_API(url, param))

print(*comments)
