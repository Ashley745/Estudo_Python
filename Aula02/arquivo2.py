import os
os.system("Clear")

arq = open("./arquivos/dados.csv","a")
nome = input("Digite o seu nome: ")
email = input("Digite seu e-mail: ")
arq.write(nome+";"+email+"\n")
arq.close()