"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC, abstractmethod

class IJanela(ABC):
    @abstractmethod
    def maximizar(self):
        pass
    
    @abstractmethod
    def minimizar(self):
        pass
    
    @abstractmethod
    def mostrar_menu(self):
        pass
        
    @abstractmethod
    def fechar(self):
        pass

class JanelaTamanhoFixo(IJanela):

    def mostrar_menu(self):
        raise NotImplementedError
    
    def fechar(self):
        raise NotImplementedError

class JanelaSemMenu(IJanela):
    
    def maximizar(self):
        raise NotImplementedError

    def minimizar(self):
        raise NotImplementedError

    def fechar(self):
        raise NotImplementedError


