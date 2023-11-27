'''
Crie um programa para mostrar se o aluno está
aprovado, reprovado ou recuperação.
O programa deve pedir 4 nostas realizar o 
cálculo da média.

    >= 6 -> Aprovado
    <= 4 -


'''
#PEdindo nota
bi1 = float ( input("Digite a nota do aluno: "))
bi2 = float( input("Digite a nota: "))
bi3 = float( input("Digite a nota: "))
bi4 = float( input("Digite a nota: "))

media = ( bi1 + bi2 + bi3 + bi4) / 4
media = float(media)
if media >=6:
    print("Aprovado")
elif media <=4:
    print("Reprovado")
else:
    print("Recuperação")