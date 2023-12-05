# import classe_dog as cl
from  classe_dog import Dog

#  Para criar o objeto
# utilizamos a váraivel pasto
# e rea lizaos o procsso de instaciação
# da classe Dog.
# foi passada o nome e idade
pastor = Dog("Bob",2)
# Acessamos o método data_dog que mostra
# os dados do cachorro
pastor.data_dog()
pastor.sit()
pastor.roll_over()
print(pastor.__class__)
print(pastor.__dict__)