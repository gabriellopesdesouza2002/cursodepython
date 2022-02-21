import os
os.system('cls' if os.name == 'nt' else 'clear')  # se o sistema for nt é csl senao clear

class Pessoa():
    ano_atual = 2022  # atributo de classe
    
    
    # construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    # método
    def get_nascimento(self):
        print(f'{self.nome} nasceu em {self.ano_atual - self.idade}')
        
        
pessoa1 = Pessoa('Gabriel', 20)



pessoa1.get_nascimento()