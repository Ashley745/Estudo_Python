# Declaração da classe cliente. Está classe permite
# que sejam criados novos objestos di tipo cliente

class Cliente:
    # A implementação do método __init__ representa a consutrução
    # do método construtor da classe, responsável por inicializar
    # o onjeto que será criado. Este método possui um argumento
    # self que faz referência a propria classe> Quando for 
    # criar um método de classe deve-se utilizar o comando 
    # self para referência a própria estrutura de classe qual
    # ele pertence
    # Note que o método __init__(construtor) foram iniciados os
    # atributos da classe, repreentando as caracteristicas do cliente
    # todos eles foram criados usando comando self, que indica
    # que eles pertecem a classe Cliente. Os atributos foram 
    # declarados como privados. Para isso utilizamos 2 undescores
     
    
    '''
    A classe Cliente gera novo clientes e pede alguns dados
    pessoais e é capaz de salvar o cliente
    '''


    def __init__(self):
     self.__nome = ""
     self.__idade = 0
     self.__genero = ""
     self.__email = ""
    # O método dados é ultilixado para realizar a passagem dos dados
    # do cliente para dentro da classe Cliente.

    def dados(self,nome="",idade=0,genero="",email=""):
        '''
        O método dados pede algumas informações do cliente para ele 
        seja salvo no sitema
        '''
        self.__nome = nome
        self.__idade = idade
        self.__genero = genero
        self.__email = email
    
    # O método gravar exibe uma mensgaem com o nome do cliente
    # dizendo que foi salvo com sucesso
    def gravar(self):
        '''
        O método gravar exibe uma mensagem com o nome cliente e 
        gravação realizada com sucesso.
        '''
        print("O cliente "+self.__nome+" foi gravado com sucesso")