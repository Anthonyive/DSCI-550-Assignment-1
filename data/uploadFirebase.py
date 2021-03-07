import requests
import os
import json

for file in range(len(os.listdir('separated_by_email'))):
    print(file)
    r = requests.put(f'https://dsci-550-default-rtdb.firebaseio.com/assignment-1/task-5-additional-features/{file}.json', json = {"index": file})
