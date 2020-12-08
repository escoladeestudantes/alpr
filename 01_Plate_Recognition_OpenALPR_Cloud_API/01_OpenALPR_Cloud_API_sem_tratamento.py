#!/usr/bin/python
#Usar
#python 01_OpenALPR_Cloud_API_sem_tratamento.py

import requests
import base64
import json

# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
IMAGE_PATH = '01.png'
#IMAGE_PATH = '02.jpg'
SECRET_KEY = 'sk_DEMODEMODEMODEMODEMODEMO' # OpenALPR
#SECRET_KEY = 'sk_533ba06333a38991b953f55a'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v3/recognize_bytes?recognize_vehicle=1&country=br&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)

#Salvar arquivo JSON
with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(r.json(), f, ensure_ascii=False, indent=2)
#with open('data2.json', 'w', encoding='utf-8') as f:
#    json.dump(r.json(), f, ensure_ascii=False, indent=2)

print(json.dumps(r.json(), indent=2))
