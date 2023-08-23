#encoding: utf-8
import json
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz
from Bots.BotHogRider import BotHogRider
from Bots.BotZiggs import BotZiggs
from Bots.BotZiggs import BotZiggs
from Bots.BotGenerico import BotGenerico
from Bots.Comando import Comando
###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Stitch"), BotFeliz("Sun"), BotHogRider("Hog Rider"), BotZiggs("Ziggs")]


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

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
