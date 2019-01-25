class grafoDirecionado():
    """docstring for grafoDirecionado"""
    listaVertices = None
    listaArestas = None
    quantVertices = None
    listaAdjacencia = None
    ''' listaAdjacencia é um dicionario que conterá uma lista de adjacencia para cada vertice(chave)'''
    def __init__(self,quantVertices, listaArestas):
        self.listaArestas = listaArestas
        self.quantVertices = quantVertices
        '''cria a lista dos vertices'''
        self.listaVertices = []
        for i in self.listaArestas:
            for j in i:
                if j not in self.listaVertices:
                    self.listaVertices.append(j)
        ''' para cada vertice na lista de vertices '''
        self.listaAdjacencia = {}
        for i in self.listaVertices:
            ''' cria-se uma lista de adjacentes'''
            adjacentes = []
            ''' jé uma lista que contem o par de vertices de cada aresta'''
            for j in self.listaArestas:
                ''' verifica os sucessores do vertice i e os adiciona na lista de adjacencia '''
                if (j[0] == i):
                    adjacentes.append(j[1])
            self.listaAdjacencia[i] = adjacentes

    ''' retorna os sucessores do vertice '''
    def listaSucessores(self, vertice):
        return self.listaAdjacencia[vertice]

    '''imprime os vertices e sua lista de adjacencia'''
    def imprimir(self):
        print('lista de adjacencia')
        '''imprime em ordem crescente'''
        self.listaVertices.sort()
        for v in self.listaVertices:
            print(v,self.listaSucessores(v))

    '''retorna a lista de vertices do grafo'''
    def getVertices(self):
        return self.listaVertices
    
    '''retorna o grau de entrada de um determinado vertice'''
    ''' grau de entrada é o numero de vertices que tem uma arestas com sentido para o vertice em questão'''
    def getGrauEntrada(self,vertice):
        grau = 0
        for v in self.listaVertices:
            if(vertice in self.listaAdjacencia[v]):
                grau += 1
        return grau
    
    '''retorna o grau de saida de um determinado vertice'''
    '''grau de saida é o numero de arestas que saem do vertice em questao ou o numero de sucessores do vertice em questao'''
    def  getGrauSaida(self, vertice):
        return len(self.listaSucessores(vertice))

    '''retorna o sucessor que tenha o menor grau de entrada'''
    def menorSucessor(self, vertice):
        listaSucessores = self.listaSucessores(vertice)
        menor = listaSucessores[0]
        for v in listaSucessores:
            if self.getGrauEntrada(v) < self.getGrauEntrada(menor):
                menor = v
        return menor
    '''remove o vertice e suas adjacencias'''
    def subgrafoInduzidoPorVertice(self,vertice):
        del self.listaAdjacencia[vertice]
