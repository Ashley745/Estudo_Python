# Criação da classe dog que dará origem 
# a vários dogs(cachorros) 

class Dog:
    # Criação da funçaõ __init__ que 
    # é responsavel por inicializar
    # o objeto que será criado.
    # Está pedindo o nome e a idade
    #  do dog no momento que ele
    # é criado.
    # Usamos o termo self para afzer uam referência
    #  a propria classe
    # Portanto, quando o criar dog e passar
    # o nome e idade, pertencerão a classe dog
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def data_dog(self):
        print(self.name)
        print(self.age)

    def sit(self):
        print("Sentou")

    def roll_over(self):
        print("Rolou")
