
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class Arvore:
    def __init__(self):
        self.raiz = None

    def obter_altura(self, no):
        if no is None:
            return 0
        else:
            return no.altura

    def atualizar_altura(self, no):
        if no is None:
            return
        altura_esquerda = self.obter_altura(no.esquerda)
        altura_direita = self.obter_altura(no.direita)
        no.altura = 1 + max(altura_esquerda, altura_direita)

    def obter_fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
            return
        
        no_atual = self.raiz
        while True:
            if valor < no_atual.valor:
                if no_atual.esquerda is None:
                    no_atual.esquerda = Node(valor)
                    break
                else:
                    no_atual = no_atual.esquerda

            elif valor > no_atual.valor:
                if no_atual.direita is None:
                    no_atual.direita = Node(valor)
                    break
                else:
                    no_atual = no_atual.direita

            else:
                break

        # -------- Parte 2 (Fase A): inserção + caminho --------
    def inserir(self, valor):
        novo_no = Node(valor)
        caminho = []

        if self.raiz is None:
            self.raiz = novo_no
            return

        no_atual = self.raiz
        while True:
            caminho.append(no_atual) # registrando o caminho

            if valor < no_atual.valor:
                if no_atual.esquerda is None:
                    no_atual.esquerda = novo_no
                    break
                no_atual = no_atual.esquerda
            elif valor > no_atual.valor:
                if no_atual.direita is None:
                    no_atual.direita = novo_no
                    break
                no_atual = no_atual.direita
            else:
                return # evita duplicatas

            

    def buscar(self, valor):
        no_atual = self.raiz
        if no_atual is None:
            return False

        while no_atual is not None:
            if valor == no_atual.valor:
                return True
            elif valor < no_atual.valor:
                no_atual = no_atual.esquerda
            else:
                no_atual = no_atual.direita

        return False
    

class Arvore_balanceada:
    
    def rotacao_direita(No_desbalanceado_Z):
        # 1. Identificar o Nó desbalanceado
        Z = No_desbalanceado_Z
        # 2. Identificar o filho da esquerda de Z, e chame-o de Y
        Y = Z.esquerda
        # 3. Identifique o filho da direita de Y, e chame-o de T3 (esta é a sub-arvore que mudara de PAI)
        T3 = Y.direita

        # Executando rotação
        Y.direita = Z
        Z.esquerda = T3

        # ATT altura
        # Primeiro chame Z pois Z está agora embaixo
        # Segundo chame Y pois Y está agora em cima
        Z.altura = 1 + max(NoArvore.altura(Z.esquerda)),max(NoArvore.altura(Z.direita))  
        Y.altura = 1 + max(NoArvore.altura(Y.esquerda)),max(NoArvore.altura(Y.direita))  
        
        return Y


# ====== TESTE SIMPLES (sem arquivo, sem lista) ======
if __name__ == "__main__":
    arvore = Arvore()

    # Inserções
    for v in (30, 20, 40, 10, 25):
        arvore.inserir(v)

    # Buscas
    print("Busca 30:", arvore.buscar(30)) # True
    print("Busca 25:", arvore.buscar(25)) # True
    print("Busca 999:", arvore.buscar(999)) # False

    # Alturas (Parte 1)
    print("Altura da raiz:", arvore.raiz.altura)
    print("Altura da esquerda:", arvore.raiz.esquerda.altura)
    print("Altura da direita:", arvore.raiz.direita.altura)

    # Fator de balanceamento (Parte 1)
    fb = arvore.obter_fator_balanceamento(arvore.raiz)
    print("Fator de balanceamento da raiz:", fb)
