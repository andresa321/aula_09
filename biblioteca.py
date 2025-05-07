class Pessoa():
    def __init__(self, nome, peso, idade):
        #atribuições
        self.nome = nome
        self.peso = peso
        self.idade = idade
        #funções
    def apresentar(self):
        print(f"ola meu nome é {self.nome}, e eu peso {self.peso} quilos e minha idade é {self.idade} anos")
    def dormir(self):
        self.dormir = True
        print(f"{self.nome} foi dormir")

    def acordar(self):
        self.comer = False
        print(f"{self.nome} esta comendo")

    def comer(self):
        if self.dormir:
            print(f"{self.nome} não pode comer pq esta dormindo")
        else:
            print(f"{self.nome} esta comendo empadão de frango, QUE DELICIA!")

