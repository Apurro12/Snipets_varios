
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt


# In[82]:


#Creo un grafo cuadrado
G = nx.grid_graph(dim = [2,2],periodic = False)
G.add_edge((1,1),(0,0))
#lista_nodos = G.nodes()


# In[83]:


#Asigno los pesos a las distintas aristas
for edge in G.edges():
    #print(edge)
    G.edges[edge]["Peso"] = 0
    #G.edges[edge[0]][edge[1]]["Peso"] = 0


# In[84]:


#Me armo los pesos
for nodo1 in G.nodes():
    for nodo2 in G.nodes():
        if nodo1 == nodo2:
            continue
        else:
            caminos_mas_cortos = list(nx.all_shortest_paths(G,nodo1,nodo2))
            cantidad_de_caminos_mas_cortos = len(caminos_mas_cortos)
            longitud_caminos_menos_uno = range(len(caminos_mas_cortos[0]) -1 )

            for camino in caminos_mas_cortos:
                for j in longitud_caminos_menos_uno:
                    G[camino[j]][camino[j+1]]["Peso"] += ( 1 / cantidad_de_caminos_mas_cortos )


# In[85]:


#a ver que onda
list(G.edges.data())


# In[86]:


colores = [G.edges[edge]["Peso"] for edge in G.edges]

nx.draw(G,with_labels=True,edge_color=colores)
plt.show()


# In[99]:


import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
i=1
G.add_node(i,pos=(i,i))
G.add_node(2,pos=(2,2))
G.add_node(3,pos=(2,1))
G.add_edge(1,2,weight=0.5)
G.add_edge(1,3,weight=9.8)
pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos,with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

