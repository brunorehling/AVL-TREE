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

    def rotacao_direita(self, z):
        y = z.esquerda
        t3 = y.direita

        y.direita = z
        z.esquerda = t3

        self.atualizar_altura(z)
        self.atualizar_altura(y)

        return y

    def rotacao_esquerda(self, z):
        y = z.direita
        t2 = y.esquerda

        y.esquerda = z
        z.direita = t2

        self.atualizar_altura(z)
        self.atualizar_altura(y)

        return y

    def inserir(self, valor):
        novo_no = Node(valor)
        caminho = []

        if self.raiz is None:
            self.raiz = novo_no
            return

        no_atual = self.raiz
        while True:
            caminho.append(no_atual)

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
                return

        for i in range(len(caminho) - 1, -1, -1):
            no_ancestral = caminho[i]

            self.atualizar_altura(no_ancestral)

            fator_balanceamento = self.obter_fator_balanceamento(no_ancestral)

            if fator_balanceamento > 1:
                filho = no_ancestral.esquerda
                if valor < filho.valor:
                    nova_sub_raiz = self.rotacao_direita(no_ancestral)
                else:
                    no_ancestral.esquerda = self.rotacao_esquerda(filho)
                    nova_sub_raiz = self.rotacao_direita(no_ancestral)

            elif fator_balanceamento < -1:
                filho = no_ancestral.direita
                if valor > filho.valor:
                    nova_sub_raiz = self.rotacao_esquerda(no_ancestral)
                else:
                    no_ancestral.direita = self.rotacao_direita(filho)
                    nova_sub_raiz = self.rotacao_esquerda(no_ancestral)

            else:
                continue

            if i == 0:
                self.raiz = nova_sub_raiz
            else:
                pai = caminho[i - 1]
                if pai.esquerda is no_ancestral:
                    pai.esquerda = nova_sub_raiz
                else:
                    pai.direita = nova_sub_raiz

            self.atualizar_altura(pai if i > 0 else self.raiz)
            break  

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


if __name__ == "__main__":
    arvore = Arvore()

    for valor in (30, 20, 40, 10, 25, 5, 35, 50, 45):
        arvore.inserir(valor)

    for valor in (30, 20, 40, 75, 10, 25, 98, 5, 35, 50, 45):
        res = arvore.buscar(valor)

        print(f"valor {valor} foi achado na árvore: {res}")

    print("Altura da raiz:", arvore.raiz.altura)
    print("Altura da esquerda:", arvore.obter_altura(arvore.raiz.esquerda))
    print("Altura da direita:", arvore.obter_altura(arvore.raiz.direita))

    fator_balanceamento = arvore.obter_fator_balanceamento(arvore.raiz)
    print("Fator de balanceamento da raiz:", fator_balanceamento)
