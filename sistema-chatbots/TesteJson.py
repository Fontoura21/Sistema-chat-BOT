import json
from Bots.Comando import Comando
from Bots.Bot import Bot
from Bots.BotGenerico import BotGenerico

lista_bots = []

with open('bots.json', 'r') as fcc_file:
    data = json.load(fcc_file)

for i in data:
    lista_comandos = []
    for comando in data[i]['lista_comandos']:
        lista_comandos.append(Comando(comando[0], comando[1], comando[2]))
    bot = BotGenerico(data[i]['name'], lista_comandos, data[i]['apresentacao'], data[i]['boas_vindas'], data[i]['despedida'])
    print(bot.nome)
    print(bot.apresentacao())
    lista_bots.append(bot)
