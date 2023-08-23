from Bots.Bot import Bot
from Bots.Comando import Comando

class BotZiggs(Bot):
    def __init__(self, nome):
        lista_comandos = [Comando(1, "Quem eh voce?", "Eu sou Ziggs"),
                    Comando(2, "Quantos anos voce existe no LoL?", "Eu circulo pelos campos da justiça durante 11 anos, desde 2012"),
                    Comando(3,"Quantas skins voce possui?", "Eu tenho 9 skin dentro de League of Legends, sendo a mais rara a skin Hextec"),
                    Comando(4, "Quem voce mais odeia?","Eu odeio aquele noxiano chamado Draven!!"),
                    Comando(5, "Adeus", "Ainda esta aqui!?")]
        super().__init__(nome,lista_comandos)


    def apresentacao(self):
        return(f"Meu nome é {super().nome} alguem quer jogar?")

    def boas_vindas(self):
        return(f"{super().nome} diz: Você me escolheu, esta partida será um estouro!")
    
    def despedida(self):
        return(f"{super().nome} diz: não acredito que nosso tempo acabou, estou indo, estou indo !!")