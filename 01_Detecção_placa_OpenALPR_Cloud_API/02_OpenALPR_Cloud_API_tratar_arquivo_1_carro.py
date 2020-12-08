#!/usr/bin/python

#Usar 
#python 02_OpenALPR_Cloud_API_tratar_arquivo_1_carro.py

import requests
import base64
import json
import cv2
import numpy as np

with open('data.json', 'r', encoding='utf8') as f:
	dados = json.load(f)

openalpr_results = dados.get("results")
openalpr_plate = openalpr_results[0]["plate"]
print('Placa: {}'.format(openalpr_plate))
openalpr_veiculo = openalpr_results[0]["vehicle"]
veiculo_cor = openalpr_veiculo['color']
print('Cor: {}'.format(veiculo_cor[0]['name']))
veiculo_make = openalpr_veiculo['make']
print('Fabricante: {}'.format(veiculo_make[0]['name']))
veiculo_body_type = openalpr_veiculo['body_type']
print('Tipo: {}'.format(veiculo_body_type[0]['name']))
veiculo_year = openalpr_veiculo['year']
print('Ano: {}'.format(veiculo_year[0]['name']))
veiculo_make_model = openalpr_veiculo['make_model']
print('Modelo: {}'.format(veiculo_make_model[0]['name']))

coordinates = openalpr_results[0]["coordinates"]
print('Coordenadas: {}'.format(coordinates))
x = []
y = []
a=0
for c in coordinates:
	x.append(coordinates[a]['x'])
	y.append(coordinates[a]['y'])
	a+=1
pts = np.array([[x[0],y[0]], [x[1],y[1]],  [x[2],y[2]], [x[3],y[3]]], np.int32) 

imagem = cv2.imread('01.png')
cv2.polylines(imagem, [pts], True, (0, 255,0), 4)
cv2.imshow('Imagem',imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()



