class Pilha:
    def __init__(self, limite):
        self.itens = []
        self.limite = limite

    def empilhar(self, item):
        if self.pilha_cheia():
            print("A pilha está cheia. Não é possível empilhar.")
            return
        self.itens.append(item)

    def desempilhar(self):
        if self.pilha_vazia():
            print("A pilha está vazia. Nada para desempilhar.")
            return None
        return self.itens.pop()

    def ver_topo(self):
        if self.pilha_vazia():
            return None
        return self.itens[-1]

    def pilha_vazia(self):
        return len(self.itens) == 0

    def pilha_cheia(self):
        return len(self.itens) == self.limite

    def tamanho(self):
        return len(self.itens)


#ex
p = Pilha(limite=8)

p.empilhar("B")
p.empilhar("E")
p.empilhar("R")
p.empilhar("N") 
p.empilhar("A") 
p.empilhar("R") 
p.empilhar("D") 
p.empilhar("O") 
print(f'a pilha é:{p.itens}')
print("Topo da pilha:", p.ver_topo())          
print("Tamanho da pilha:", p.tamanho())        
print("A pilha está vazia?", p.pilha_vazia())   
print("A pilha está cheia?", p.pilha_cheia())   
p.desempilhar()
p.desempilhar()
p.desempilhar()
print(f'a nova pilha após o desempilhar é {p.itens}')
print("Topo da pilha:", p.ver_topo()) 
     
