#vetor não ordenado

class Vetor:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.valores = [None] * capacidade
        self.ultima_posicao = -1

    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Mensagem de vetor cheio")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def imprimir(self):
        if self.ultima_posicao == -1:
            print("Mensagem de vetor vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
#ex
v = Vetor(9)
v.inserir('B')
v.inserir('E')
v.inserir('R')
v.inserir('N')
v.inserir('A')
v.inserir('R')
v.inserir('D')
v.inserir('O')
v.imprimir()


print(f'o  valor pesquisado é{v.pesquisar('B')}')  
print(f'o  valor pesquisado é{v.pesquisar('E')}') 
print(f'o  valor pesquisado é{v.pesquisar('D')}') 
v.excluir('B')
v.excluir('A')
v.excluir('O')
v.imprimir()


