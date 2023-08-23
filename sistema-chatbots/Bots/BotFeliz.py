from Bots.Bot import Bot
from Bots.Comando import Comando

class BotFeliz(Bot):
    def __init__(self,nome):
        self.__nome = nome

        lista_comando = [Comando(1, "Bom Dia!", 'BOM DIA! MAS QUE LINDO DIA!'),
                         Comando(2, "Qual o seu nome?", "Normamente me chamam de idiota, burro... Mas meu nome verdadeiro é "+self.nome),
                         Comando(3, "Quero um Conselho.", "Até mais, esterei sempre aqui para mais conversas!"),
                         Comando(4, "Adeus", "Até mais, esterei sempre aqui para mais conversas!")]

        super().__init__(nome, lista_comando)

    @property
    def nome(self):
        return self.__nome

    def apresentacao(self) -> str:
        return ":) Meu nome é "+self.nome+", seja MUITOOOO BEM VINDOOO! Estou muito feliz!!"

    def boas_vindas(self) -> str:
        return self.nome+" diz: Fico muito feliz que me escolheu, melhor dia de sempre!"

    def despedida(self) -> str:
        return self.nome+" diz: 'Que pena que vai embora, gostei muito de falar com voce!'"
