import funcoes_auxiliares_ponderadas as fa

class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai = pai
        self.estado = estado
        self.valor1 = valor1
        self.valor2 = valor2
        self.anterior = anterior
        self.proximo = proximo

class lista(object):
    head = None
    tail = None

    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head is None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    def insereUltimo(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
        self.tail = novo_no

    def inserePos_X(self, s, v1, v2, p):
        if self.head is None:
            self.inserePrimeiro(s, v1, v2, p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break
            if atual == self.head:
                self.inserePrimeiro(s, v1, v2, p)
            elif atual is None:
                self.insereUltimo(s, v1, v2, p)
            else:
                novo_no = No(p, s, v1, v2, None, None)
                aux = atual.anterior
                aux.proximo = novo_no
                novo_no.anterior = aux
                atual.anterior = novo_no
                novo_no.proximo = atual

    def deletaPrimeiro(self):
        if self.head is None:
            return None
        no = self.head
        self.head = self.head.proximo
        if self.head is not None:
            self.head.anterior = None
        else:
            self.tail = None
        return no

    def deletaUltimo(self):
        if self.tail is None:
            return None
        no = self.tail
        self.tail = self.tail.anterior
        if self.tail is not None:
            self.tail.proximo = None
        else:
            self.head = None
        return no

    def vazio(self):
        return self.head is None

    def exibeArvore2(self, s, v1):
        atual = self.tail
        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho[::-1]  

class busca(object):

    def custo_uniforme(self, inicio, fim, mapa, dx, dy):
        return self._executa_busca(inicio, fim, mapa, dx, dy, tipo='custo')

    def greedy(self, inicio, fim, mapa, dx, dy):
        return self._executa_busca(inicio, fim, mapa, dx, dy, tipo='greedy')

    def a_estrela(self, inicio, fim, mapa, dx, dy):
        return self._executa_busca(inicio, fim, mapa, dx, dy, tipo='a*')

    def aia_estrela(self, inicio, fim, mapa, dx, dy, limite):
        while True:
            caminho, custo, lim_exc = self._executa_busca(inicio, fim, mapa, dx, dy, tipo='a*', limite=limite)
            if caminho:
                return caminho, custo
            if not lim_exc:
                break
            limite = float(sum(lim_exc) / len(lim_exc))
        return [], None

    def _executa_busca(self, inicio, fim, mapa, dx, dy, tipo='a*', limite=float('inf')):
        l1 = lista()
        l2 = lista()
        visitado = []
        lim_excedidos = []
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        visitado.append([inicio, 0])

        while not l1.vazio():
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = l2.exibeArvore2(atual.estado, atual.valor1)
                return caminho, atual.valor2, lim_excedidos

            filhos = fa.sucessores(atual.estado, mapa, dx, dy)
            for novo in filhos:
                valor = [novo[0], novo[1]]
                v2 = atual.valor2 + novo[2]

                if tipo == 'custo':
                    v1 = v2
                elif tipo == 'greedy':
                    v1 = fa.h(valor, fim)
                else:
                    v1 = v2 + fa.h(valor, fim)

                if v1 > limite:
                    lim_excedidos.append(v1)
                    continue

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == valor:
                        if visitado[j][1] <= v2:
                            flag1 = False
                        else:
                            visitado[j][1] = v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, atual)
                    l2.insereUltimo(valor, v1, v2, atual)
                    if flag2:
                        visitado.append([valor, v2])
        return [], None, lim_excedidos
