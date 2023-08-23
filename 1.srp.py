"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    # salva no DB
    def save(self, animal: Animal):
        pass
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

class ToSave:    
    def __init__(self, object_) -> None: 
        self.save(object_)

    def save(self, object):
        pass