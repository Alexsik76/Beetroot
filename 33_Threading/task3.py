# Requests using multiprocessing
import requests
import threading
# import json

url = "https://api.pushshift.io/reddit/comment/search/"
comments = []
authors = ["Yurishirox", "Zeewitje", "Magic-Prankster"]
# authors = ["Yurishirox"]
# key_list = ['id', 'author', 'body']


def read_from_API(url: str, param: str):
    reqest = requests.get(f'{url}{param}')
    thead = {'thead': threading.current_thread().getName()}
    data_to_add = reqest.json()['data']
    for item in data_to_add:
        item.update(thead)
    return data_to_add


threads = []
for author in authors:
    param = f'?author={author}&filter=author,id,body'
    t = threading.Thread(target=read_from_API, args=(url, param))
    threads.append(t)
    t.start()

for thread in threads:
    comments.append(thread)
    print(type(thread))
    print(dir(thread))
    print(thread[0])

print(*comments)



from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
values = [2,3,4,5]
def square(n):
   return n * n
def main():
   with ThreadPoolExecutor(max_workers = 3) as executor:
      results = executor.map(square, values)
for result in results:
      print(result)
if __name__ == '__main__':
   main()