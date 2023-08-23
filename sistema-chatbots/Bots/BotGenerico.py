from Bots.Bot import Bot
from Bots.Comando import Comando

class BotGenerico(Bot):
    def __init__(self,nome, lista_comando, apresentacao, boas_vindas, despedida):
        self.__nome = nome
        self.__apresentacao = apresentacao
        self.__boas_vindas = boas_vindas
        self.__despedida = despedida


        super().__init__(nome, lista_comando)

    @property
    def nome(self):
        return self.__nome

    def apresentacao(self) -> str:
        return self.__apresentacao

    def boas_vindas(self) -> str:
        return self.__boas_vindas

    def despedida(self) -> str:
        return self.__despedida
