#usar o comando de importção para biblioteca criada
import ctypes

lib = ctypes.CDLL("./mensagem.so")
lib.mensagem()