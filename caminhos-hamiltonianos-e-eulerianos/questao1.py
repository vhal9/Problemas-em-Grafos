'''
    este algoritmo encontra  a solucao para a questao1 do arquivo ProblemasGrafosEulerianoHamiltonianos.pdf
    este problema foi proposto na disciplina de Grafos da UFLA pelo professor Dr Mayron Cesar de Oliveira Moreira
    o grafo de entrada para este algoritmo é um grafo orientado que nao contem ciclos
'''
from grafo import grafoDirecionado

''' funcao retorna lista de cada linha do arquivo '''
def LerArquivo():
    #nomeArquivo = input('entre com o nome do arquivo:')
    nomeArquivo = 'exemplo1.txt'
    arquivo = open(nomeArquivo, 'r')
    conteudo = []
    for linha in arquivo:
        linha = linha.rstrip()
        conteudo.append(linha)
    return conteudo

''' funcao retorna uma lista com cada aresta do grafo - cada aresta é uma lista'''
def LerArestas(arquivo):
    arestas = []
    for aresta in arquivo:
        arestas.append(aresta.split())
    return arestas
'''se mais de um vertice tiver grau de entrada igual a 0, o grafo é desconexo, portanto não tem solução'''
def testeDoGrauDeEntrada(grafo):
    listaVertices = grafo.getVertices()
    quantVerticesSolucao = 0
    
    for vertice in listaVertices:
        if grafo.getGrauEntrada(vertice) == 0:
            quantVerticesSolucao += 1

    if(quantVerticesSolucao != 1):
        return False
    '''se nao ha mais de um vertice com grau de entrada igual a 0, pode haver uma solucao '''
    return True

'''função percorre o grafo, buscando uma solução começando pelo vertice de grau de entrada igual à 0 e percorrendo o grafo'''
'''com critério de que o próximo vertice é o sucessor de menor grau de entrada'''
def percorrer(grafo, quantVertices):
    listaVertices = grafo.getVertices()
    vertice = 0
    '''encontra o primeiro vertice, o que tem grau de entrada igual a 0'''
    for v in listaVertices:
        if grafo.getGrauEntrada(v) == 0:
            vertice = v
    '''adiciona v na saida e remove ele da lista de vertices do grafo'''
    listaSaida = []
    listaSaida.append(vertice)
    listaVertices.remove(vertice)

    '''enquanto a lista de vertices não esta vazia e o vertice atual tem grau de saida maior que 0, ou seja, tem sucessores'''
    '''percorre o grafo, indo para o próximo vertice que contém o menor grau de entrada na lista de sucessores do vertice atual'''
    '''adicionando os vertices na lista de saida na ordem em que são percorridos e removendo-os da lista de vertices'''
    while len(listaVertices) != 0 and grafo.getGrauSaida(vertice) > 0:
        menorSucessor = grafo.menorSucessor(vertice)
        grafo.subgrafoInduzidoPorVertice(vertice)
        vertice = menorSucessor
        listaSaida.append(vertice)
        listaVertices.remove(vertice)
    return listaSaida
'''funcao principal'''
def main():
    arquivo = LerArquivo()

    quantVertices = int(arquivo.pop(0))
    listaArestas = LerArestas(arquivo)

    grafo = grafoDirecionado(quantVertices, listaArestas)
    '''grafo.imprimir()'''

    '''Alguns testes para verificar se há solução'''
    solucao = testeDoGrauDeEntrada(grafo)
    if not solucao:
        print('Solucao nao pode ser encontrada')
    else:
        listaSaida = percorrer(grafo, quantVertices)
        '''Se a lista de saida possui todos os vertices do grafo, houve solução'''
        if (len(listaSaida) == quantVertices):
            print('Solucao = ', listaSaida)
        else:
            print('Solucao nao encontrada')

main()