class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor, end=' ')


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if not self.primeiro:
            print("Erro: lista vazia")
            return

        atual = self.primeiro
        while atual:
            atual.mostrar_no()
            atual = atual.proximo
        print()

    def excluir_inicio(self):
        if not self.primeiro:
            print("Erro: lista vazia")
            return None

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        print(f"Excluído do início: {temp.valor}")
        return temp

    def pesquisar(self, valor):
        if not self.primeiro:
            print("Erro: lista vazia")
            return None

        atual = self.primeiro
        while atual:
            if atual.valor == valor:
                print(f"Valor '{valor}' encontrado.")
                return atual
            atual = atual.proximo

        print(f"Valor '{valor}' não encontrado.")
        return None

    def excluir_qualquer(self, valor):
        if not self.primeiro:
            print("Erro: lista vazia")
            return None

        atual = self.primeiro
        anterior = None

        while atual and atual.valor != valor:
            anterior = atual
            atual = atual.proximo

        if not atual:
            print(f"Valor '{valor}' não encontrado para exclusão.")
            return None

        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo

        print(f"Valor '{valor}' excluído.")
        return atual


# Exemplo de uso
l = ListaEncadeada()
l.inserir_inicio('O')
l.inserir_inicio('D')
l.inserir_inicio('R')
l.inserir_inicio('A')
l.inserir_inicio('N')
l.inserir_inicio('R')
l.inserir_inicio('E')
l.inserir_inicio('B')

l.mostrar()
l.excluir_inicio()
l.mostrar()
l.pesquisar('O')
l.excluir_qualquer('R')
l.mostrar()
