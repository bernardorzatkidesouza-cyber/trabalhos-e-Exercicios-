#vetor ordenado
class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.valores = [None] * capacidade
        self.ultima_posicao = -1

    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Mensagem de Vetor Cheio')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('Mensagem de vetor vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'{i} - {self.valores[i]}')

    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
        return -1

    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            if limite_inferior > limite_superior:
                return -1

            posicao_atual = (limite_inferior + limite_superior) // 2

            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif self.valores[posicao_atual] < valor:
                limite_inferior = posicao_atual + 1
            else:
                limite_superior = posicao_atual - 1

    def excluir(self, valor):
        posicao = self.pesquisa_linear(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

#ex

v = VetorOrdenado(9)
v.inserir('B')
v.inserir('E')
v.inserir('R')
v.inserir('N')
v.inserir('A')
v.inserir('R')
v.inserir('D')
v.inserir('O')
v.imprimir()


print(f'o  valor pesquisado é {v.pesquisa_linear('B')}')  
print(f'o  valor pesquisado é {v.pesquisa_linear('E')}') 
print(f'o  valor pesquisado é {v.pesquisa_linear('D')}') 
v.excluir('B')
v.excluir('A')
v.excluir('O')
v.imprimir()