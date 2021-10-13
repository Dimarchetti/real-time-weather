import requests
import json

cidade = input('Qual o nome da sua Cidade? ')

req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=65b38c99811f47c1e117b2f4bcc87ca6')

tempo = json.loads(req.text)
cond_tempo = tempo['weather'][0]['main']
temperatura = tempo['main']['temp'] -273.15

print('Condição do tempo:', cond_tempo)
print('Temperatura:', float(round(temperatura, 2)),'graus Celsius')