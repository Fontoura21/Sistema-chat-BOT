from Bots.Bot import Bot
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
        self.working = True
        self.working2 = True

    
    def boas_vindas(self) -> None:
        print()
        print(f"Bem-vindo ao {self.__empresa}!")
        print()

    def mostra_menu(self) -> None:
        print(f"Os chat bots disponíveis para conversa são:")
        count = 1
        for bot in self.__lista_bots:
            print(f'{count} - {bot.apresentacao()}') 
            count += 1
    
    def escolhe_bot(self) -> None: 
        self.working2 = True
        while True:
            try:
                escolha = int(input("Escolha o bot que deseja conversar! (-1 para sair do programa): "))
            except Exception as e:
                print()
                print(e)
                self.working2 = False
                print()
                return None

            print()

            if (escolha == -1):
                self.working = False
                self.working2 = False
                return None

            if (escolha < 1) or (escolha > len(self.__lista_bots)): 
                print('Erro! Escolha um valor válido.')
            else:
                self.__bot = self.__lista_bots[escolha-1] 
                print(self.__bot.boas_vindas())
                break


    def mostra_comandos_bot(self) -> None:
        print() 
        ##mostra os comandos disponíveis no bot escolhido
        print(self.__bot.mostra_comandos())


    def le_envia_comando(self) -> None:
        try:
            escolha = int(input("Digite o comando desejado (ou -1 fechar o sistema sair): "))
        except Exception as e:
            print()
            print(e)
            return None
        else:
            if (escolha == -1):
                self.working = False
                self.working2 = False
                return None

            print()
            print(self.__bot.executa_comando(escolha))
            if (escolha == len(self.__bot.lista_comandos)):
                self.working2 = False
                return None
        
    def inicio(self):
        
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
        while self.working:

            self.boas_vindas()
            self.mostra_menu()

            self.escolhe_bot()

            while self.working2:
                self.mostra_comandos_bot()

                self.le_envia_comando()

        print("Fim do programa!")

