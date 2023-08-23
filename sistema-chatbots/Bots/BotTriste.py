from Bots.Bot import Bot
from Bots.Comando import Comando

class BotTriste(Bot):
    def __init__(self,nome):
        self.__nome = nome

        lista_comando = [Comando(1, "Bom Dia!", 'Queria eu que fosse um bom dia...'),
                         Comando(2, "Qual o seu nome?", "Normamente me chamam de idiota, burro... Mas meu nome verdadeiro é "+self.nome),
                         Comando(3, "Quero um Conselho.", "Também estou precisando, mas até agora nada :(."),
                         Comando(4, "Adeus", "Mas um dia sozinho... Estou acostumado.")]

        super().__init__(nome, lista_comando)

    @property
    def nome(self):
        return self.__nome

    def apresentacao(self) -> str:
        return ":( Meu nome é "+self.nome+", seja bem vindo, eu acho... :c"
 
    def boas_vindas(self) -> str:
        return self.nome+" diz: Aleluia alguém me escolheu, não aguentava mais essa solidão..."

    def despedida(self) -> str:
        return self.nome+" diz: 'NAAAAAAAAAAAAAO, por favor :c '"
