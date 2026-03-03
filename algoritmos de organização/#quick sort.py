#quick sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista  # já está ordenada

    pivô = lista[0]  # escolhe o primeiro elemento como pivô
    menores = [x for x in lista[1:] if x <= pivô]
    maiores = [x for x in lista[1:] if x > pivô]

    return quick_sort(menores) + [pivô] + quick_sort(maiores)