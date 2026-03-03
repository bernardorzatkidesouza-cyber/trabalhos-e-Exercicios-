#bubblesort
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

#ex
numeros = [5, 3, 8, 4, 2]
print("Antes da ordenação:", numeros)
inicio = time.time()
bubble_sort(numeros)
fim = time.time()

print("Depois da ordenação:", numeros)
print(f"Tempo de execução: {fim - inicio:.6f} segundos")


#insertionsort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

#ex
numeros = [5, 3, 8, 4, 2]
print("Antes da ordenação:", numeros)
inicio = time.time()
insertion_sort(numeros)
fim = time.time()

print("Depois da ordenação:", numeros)
print(f"Tempo de execução: {fim - inicio:.6f} segundos")


