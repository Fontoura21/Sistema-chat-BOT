from Bots.Bot import Bot
from Bots.Comando import Comando

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome

        lista_comando = [Comando(1, "Bom Dia!", 'Bom dia pra quem?'),
                         Comando(2, "Qual o seu nome?", "Não te interessa! Mas é "+self.nome),
                         Comando(3, "Quero um Conselho.", "Pergunda pro seu pai!"),
                         Comando(4, "Adeus", "Ainda esta aqui!?")]

        super().__init__(nome, lista_comando)

    @property
    def nome(self):
        return self.__nome

    def apresentacao(self) -> str:
        return ">:( Meu nome é "+self.nome+", seja mal vindo GRRRR!"
 
    def boas_vindas(self) -> str:
        return self.nome+" diz: Eu não posso acreditar que me escolheu!, GRRRRRRRRR!"

    def despedida(self):
        return self.nome+" diz: 'Finalmente, já estava na hora! GRRR'"
