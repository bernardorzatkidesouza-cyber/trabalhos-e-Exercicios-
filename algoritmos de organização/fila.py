class Fila:
    def __init__(self, limite):
        self.itens = []
        self.limite = limite

    def enfilerar(self, item):
        if self.fila_cheia():
            print("A fila está cheia. Não é possível enfilerar.")
            return
        self.itens.append(item)

    def desemfilerar(self):
        if self.fila_vazia():
            print("A fila está vazia. Nada para desemfilerar.")
            return None
        return self.itens.pop(0)

    def ver_final(self):
        if self.fila_vazia():
            return None
        return self.itens[-1]
    def ver_inicio(self):
        if self.fila_vazia():
            return None
        return self.itens[0]

    def fila_vazia(self):
        return len(self.itens) == 0

    def fila_cheia(self):
        return len(self.itens) == self.limite

    def tamanho(self):
        return len(self.itens)
    

#ex
f = Fila(limite=8)
f.desemfilerar()
f.enfilerar("B")
f.enfilerar("E")
f.enfilerar("R")
f.enfilerar("N") 
f.enfilerar("A") 
f.enfilerar("R") 
f.enfilerar("D") 
f.enfilerar("O") 
print(f'a fila é:{f.itens}')
print("final da fila:", f.ver_final())          
print("Tamanho da fila:", f.tamanho())        
f.enfilerar("O") 
print("inicio da fila:", f.ver_inicio()) 
f.desemfilerar()
f.desemfilerar()
f.desemfilerar()
print(f'a nova fila após o desenfilerar é {f.itens}')
print("inicio da fila:", f.ver_inicio()) 
     
