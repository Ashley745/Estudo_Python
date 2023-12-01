def soma(valores):
    """Soma realiza a soma do valores que estão 
    em uma lista retorna o resultado da soma"""
    rs = 0
    for i in valores:
        rs+=i
    return rs

def media(valores):
    """A função média realiza a soma dos valores 
    e devide pela quantidade de valore somados e 
    retorna o resultado"""
    rs = 0
    qtd = len(valores)
    for i in valores:
        rs+=i
    return rs/qtd

def maior(valores):
    """A função maior retorna o maior valor de uma lista"""
    m = valores[0]
    for i in valores:
        if i > m:
            m = i
    return m

def menor(valores):
    """A função menor retorna o menor valor da lsita"""
    m = valores[0]
    for i in valores:
        if i < m:
            m = i
    return m