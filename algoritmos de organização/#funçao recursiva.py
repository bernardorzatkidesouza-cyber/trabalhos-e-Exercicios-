#funçao recursiva
#ex 1
#a
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma_lista(lista[1:])
#b
def maximo_lista(lista):
    if len(lista) == 1:
        return lista[0]
    return max(lista[0], maximo_lista(lista[1:]))
#c
def minimo_lista(lista):
    if len(lista) == 1:
        return lista[0]
    return min(lista[0], minimo_lista(lista[1:]))
#d
def media_lista(lista):
    if len(lista) == 0:
        return 0
    return soma_lista(lista)/len(lista)
#2
def soma_num(valor):
    if valor==1 or valor==0:
        return valor
    return valor+soma_num(valor-1)
#3
def fibonacci_num(valor):
    if valor==1 or valor==0:
        return valor
    return (valor-1)+(valor-2)
#4
def fatorial(valor):
    if valor==1 or valor==0:
        return 1
    return valor*fatorial(valor-1)
#5
def Multip_Rec(n1, n2):
    if n2 == 0:
        return 0
    if n2 < 0:
        return -Multip_Rec(n1, -n2)
    return n1 + Multip_Rec(n1, n2 - 1)
#6
def imprimir_decrescente(valor):
    if valor < 0:
        return valor
    print(valor)
    if valor > 0:
        imprimir_decrescente(valor - 1)
#7
def imprimir_pares(valor):
    if valor < 0:
        return
    imprimir_pares(valor - 2)
    print(valor)