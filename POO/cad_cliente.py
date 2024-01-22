from class_cliente import Cliente

nome = input("Digite nome do Cliente: ")
email = input("Digite o email do Cliente: ")
cpf = input ("Digite o cpf do Cliente: ")
idade = input("Digite a idade do Cliente: ")
telefone = input("Digite o telefone do Cliente: ")

# Vamos instaciar a classe Cliente. Gerar um objeto
# a partir da classe Cliente passando todas as 
# propriedades para objeto criado 
cli = Cliente()
cli.gravarCliente(nome,email,cpf,idade,telefone)

