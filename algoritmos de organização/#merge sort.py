# merge sort
def merge_sort(lista):
    # Divisão da lista
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        # Chamada recursiva para as sublistas
        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        # Combina as listas esquerda e direita de forma ordenada
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1  # Fora do if/else, sempre incrementa

        # Copia os elementos restantes da esquerda (se houver)
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        # Copia os elementos restantes da direita (se houver)
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

    return lista

# Teste
num = [38, 27, 43, 3, 9, 82, 10]
merge_sort(num)
print(num)
