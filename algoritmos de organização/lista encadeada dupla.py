class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostrar_no(self):
        print(self.valor, end=' ')

class LDP:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def lista_vazia(self):
        return self.primeiro is None

    def inserir_inicio(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.primeiro = self.ultimo = novo
        else:
            novo.proximo = self.primeiro
            self.primeiro.anterior = novo
            self.primeiro = novo

    def inserir_final(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.primeiro = self.ultimo = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
            self.ultimo = novo

    def excluir_inicio(self):
        if self.lista_vazia():
            return None
        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.primeiro = self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo
            self.primeiro.anterior = None
        return temp

    def excluir_final(self):
        if self.lista_vazia():
            return None
        temp = self.ultimo
        if self.primeiro.proximo is None:
            self.primeiro = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.proximo = None
        return temp

    def excluir_qualquer(self, valor):
        if self.lista_vazia():
            return None

        atual = self.primeiro
        while atual and atual.valor != valor:
            atual = atual.proximo

        if atual == None:
            return None  

        if atual == self.primeiro:
            return self.excluir_inicio()
        elif atual == self.ultimo:
            return self.excluir_final()
        else:
            atual.anterior.proximo = atual.proximo
            atual.proximo.anterior = atual.anterior
            return atual

    def mostrar_inicio(self):
        atual = self.primeiro
        while atual:
            atual.mostrar_no()
            atual = atual.proximo
        print()

    def mostrar_final(self):
        atual = self.ultimo
        while atual:
            atual.mostrar_no()
            atual = atual.anterior
        print()

    def pesquisar(self, valor):
        if self.lista_vazia():
            print('Erro: lista vazia')
            return None

        atual = self.primeiro
        while atual:
            if atual.valor == valor:
                return atual
            atual = atual.proximo
        return None

#ex

l=LDP()
l.inserir_inicio('O')
l.inserir_inicio('D')
l.inserir_inicio('R')
l.inserir_inicio('A')
l.inserir_inicio('N')
l.inserir_inicio('R')
l.inserir_inicio('E')
l.inserir_inicio('B')
l.mostrar_inicio()
l.excluir_inicio()
l.mostrar_inicio()
l.pesquisar('O')
l.excluir_qualquer('A')
l.mostrar_inicio()


