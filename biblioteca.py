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

class Animal():
            def __init__(self,nome,cor):
                self.nome=nome
                self.cor=cor

            def comer(self):
                print(f" O {self.nome} foi comer...")

class Gato(Animal):
            def __init__(self,nome,cor):
                super().__init__(nome,cor)
            def miar(self):
                print(f" O {self.nome} esta miando")

class Cachorro(Animal):
            def __init__(self,nome,cor):
                super().__init__(nome,cor)
            def latir(self):
                print(f" O {self.nome} ta latindo muito")

class Coelho(Animal):
            def __init__(self, nome, cor):
                super().__init__(nome, cor)

            def chiar(self):
                print(f" O {self.nome} ta chiando")

class Vaca(Animal):
            def __init__(self, nome, cor):
                super().__init__(nome, cor)

            def mujir(self):
                print(f" O {self.nome} ta mujindo")

class Ingresso():
    def __init__(self, valor):
        self.valor=valor
    def imprimirvalor(self):
        print(f"o valor do imgresso é {self.valor}")

class Vip(Ingresso):
    def __init__(self, valor):
#pode fazer a multiplicacao pq o valor é 50%
        super().__init__(valor*1,5)
    def imprimirvalor(self):
        print(f"o valor do imgresso Vip é {self.valor}")

class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0

class Retangulo(Forma):
    def __init__(self,base,altura):
        super().__init__()
    def calculaArea(self):
        area = base * altura


