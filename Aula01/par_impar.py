numero = input("Digite um número: ")
# o comando input sempre retorna um valor
#em formato de texto. Não importa se foi digitado
#um número. Ele sempre retorna um texto
#Sendo assim, foi necessário converter
#número para um valor inteiro. Utilizamos o
#comando int(inteiro)


if int(numero) % 2 == 0:
    print("O número digitado é par")
else:
    print("O número é impar")
