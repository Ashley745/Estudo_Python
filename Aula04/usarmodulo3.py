
# PAra importar apenas uma função dentro de 
# um modulo, usamos o comando from para indicar 
# o nomde do módulo e o comando importa para
# usar apenas uma função. Você também pode 
# aplicar um alias para função importada

import usarmodulo4
chat = "Estou aprendendo os comandos python"
print(chat)
enc = (usarmodulo4.caesar(chat, 18))
print(enc)
print(usarmodulo4.caesar(enc, 18, decode = True))