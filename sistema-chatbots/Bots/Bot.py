##implemente as seguintes classes

from abc import ABC, abstractmethod
from Bots.Comando import Comando

class Bot(ABC):
    def __init__(self, nome: str, lista_comando: list[Comando]):
        self.__nome = nome

        self.__lista_comandos = lista_comando


    @property
    def lista_comandos(self):
        return self.__lista_comandos

    @property
    def nome(self):
        return self.__nome


    def mostra_comandos(self) -> str:
        comandos = ""
        for x in self.lista_comandos:
           comandos += f"{x.cmd} - {x.pergunta} \n" 

        return comandos

    def executa_comando(self, cmd: int) -> str:
        for x in self.lista_comandos:
            if (x.cmd == cmd):
                resposta = f"{self.nome} diz: Voce disse: '{x.pergunta}' \n"
                resposta += f"Eu te respondo: '{x.resposta}'"

                return resposta
        else:
            return "ERROR: Opção invalida!"

    @abstractmethod
    def boas_vindas() -> str:
        pass
    
    @abstractmethod
    def despedida() -> str:
        pass
