import math
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b
def raiz(a):
    if a < 0:
        return "Erro! Não há raiz de números negativos."
    return math.sqrt(a)
def potencia(a, b):
    return a ** b