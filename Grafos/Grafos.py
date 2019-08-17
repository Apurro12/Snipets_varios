import networkx as nx
import matplotlib.pyplot as plt


#Creo un grafo cuadrado
G = nx.grid_graph(dim = [2,2],periodic = False)
lista_nodos = G.nodes()



#Aca defino el diccionario pesos, estan todos los caminos, idas y vueltas#
pesos = {}
for nodo1 in lista_nodos:
	for edges_nodo_1 in G.edges(nodo1):
#		print("El " + str(nodo1) + " se conecta con " + str(edges_nodo_1[-1]))
		pesos[edges_nodo_1] = 0



for nodo1 in lista_nodos:
	for nodo2 in lista_nodos:
		if nodo1 == nodo2:
			continue
		else:
			caminos_mas_cortos = list(nx.all_shortest_paths(G,nodo1,nodo2))
			cantidad_de_caminos_mas_cortos = len(caminos_mas_cortos)
			longitud_caminos_menos_uno = range(len(caminos_mas_cortos[0]) -1 )

			for camino in caminos_mas_cortos:
				for j in longitud_caminos_menos_uno:
					pesos[(camino[j],camino[j+1])] += ( 1 / cantidad_de_caminos_mas_cortos )




###Ahora sabieno que es no direccionado, junto los caminos de ida y vuelta
#edges_duplicados = pesos.keys()
#for key_1 in edges_duplicados:
#	for key_2 in edges_duplicados:
#		if key_2 == key_1:
#			continue

nx.draw(G,with_labels=True)
plt.show()