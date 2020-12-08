#!/usr/bin/python

#Usar 
#python 03_OpenALPR_Cloud_API_tratar_arquivo_carros.py

import requests
import base64
import json
import cv2

with open('data3.json', 'r', encoding='utf8') as f:
	dados = json.load(f)

openalpr_results = dados.get("results")

quantidade_placas = len(openalpr_results)

resultado = {}
info_geral = {}

for x in range(quantidade_placas):
	openalpr_plate = openalpr_results[x]["plate"]
	openalpr_veiculo = openalpr_results[x]["vehicle"]
	veiculo_cor = openalpr_veiculo['color']
	veiculo_make = openalpr_veiculo['make']
	veiculo_body_type = openalpr_veiculo['body_type']
	veiculo_year = openalpr_veiculo['year']
	veiculo_make_model = openalpr_veiculo['make_model']
	info_geral['Placa'] = openalpr_plate
	info_geral['Cor'] = veiculo_cor[0]['name']
	info_geral['Fabricante'] = veiculo_make[0]['name']
	info_geral['Tipo'] = veiculo_body_type[0]['name']
	info_geral['Ano'] = veiculo_year[0]['name']
	info_geral['Modelo'] = veiculo_make_model[0]['name']
	resultado['Veiculo {}'.format(x+1)] = info_geral
	info_geral = {}

print(resultado)
print(resultado['Veiculo 1'])
print(resultado['Veiculo 1']['Placa'])

open('dicionario.json','w').write(json.dumps(resultado))

