import sys, os, time
import networkx as nx

def dominant(g):
    """
        A Faire:         
        - Ecrire une fonction qui retourne le dominant du graphe non dirigé g passé en parametre.
        - cette fonction doit retourner la liste des noeuds d'un petit dominant de g

        :param g: le graphe est donné dans le format networkx : https://networkx.github.io/documentation/stable/reference/classes/graph.html

    """
    G = nx.Graph()
    # gedges = list(g.edges)
    listnode = list(g.nodes)
    for nd in listnode:
        attrs = {nd: {'fc': -1}} 
        nx.set_node_attributes(g, attrs)
    # g.graph['fc'] = -1
    # print(list(g.nodes(data=True)))

    # while g.number_of_nodes() != 0:
    #     listnode = list(g.nodes)
    #     for nd in listnode:
    #         g.node[nd]['fc'] = -1
    nodefc = -1
    while nodefc != 0 :
        listnode = list(g.nodes)
        maxdegree = -1
        nodemaxd = '0'
        for i in range(len(listnode)):
            node = listnode[i]
            if g.degree[node] > maxdegree and g.nodes[node]['fc'] != 0:
                maxdegree = g.degree[node]
                nodemaxd = node
        # if maxdegree != -1:
        G.add_node(nodemaxd)
        nodemxnb = list(g[nodemaxd])
        for j in range(len(nodemxnb)):
            g.nodes[nodemxnb[j]]['fc'] = 0
        g.remove_edges_from(list(g.edges(nodemaxd)))
        g.remove_node(nodemaxd)
        nodefc = 0
        listnode = list(g.nodes)
        for nd in listnode:
            if g.node[nd]['fc'] == -1:
                nodefc = -1
    return G.nodes # pas terrible :) mais c'est un dominant



# def dominant(g):
#     G = nx.Graph()
#     while g.number_of_nodes() != 0 :
#         listnode = list(g.nodes)
#         maxdegree = -1
#         nodemaxd = '0'
#         for i in range(len(listnode)):
#             nodedegr = 0
#             node = listnode[i]
#             listnode2 = list(g[node])
#             nodedegr += g.degree[node]
#             for j in range(len(listnode2)):
#                 node2 = listnode2[j]
#                 nodedegr += g.degree[node2]-1
#             if nodedegr > maxdegree:
#                 maxdegree = nodedegr
#                 nodemaxd = node
#         G.add_node(nodemaxd)
#         g.remove_nodes_from(list(g[nodemaxd]))
#         g.remove_node(nodemaxd)
#     return G.nodes


# def dominant(g):
#     G = nx.Graph()
#     while g.number_of_nodes() != 0 :
#         listnode = list(g.nodes)
#         maxdegree = -1
#         nodemaxd = '0'
#         for i in range(len(listnode)):
#             node = listnode[i]
#             if g.degree[node] - maxdegree > 0:
#                 maxdegree = g.degree[node]
#                 nodemaxd = node
#         G.add_node(nodemaxd)
#         g.remove_nodes_from(list(g[nodemaxd]))
#         g.remove_node(nodemaxd)
#     return G.nodes

#########################################
#### Ne pas modifier le code suivant ####
#########################################
if __name__=="__main__":
    input_dir = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2])
    
    # un repertoire des graphes en entree doit être passé en parametre 1
    if not os.path.isdir(input_dir):
	    print(input_dir, "doesn't exist")
	    exit()

    # un repertoire pour enregistrer les dominants doit être passé en parametre 2
    if not os.path.isdir(output_dir):
	    print(input_dir, "doesn't exist")
	    exit()       
	
    # fichier des reponses depose dans le output_dir et annote par date/heure
    output_filename = 'answers_{}.txt'.format(time.strftime("%d%b%Y_%H%M%S", time.localtime()))             
    output_file = open(os.path.join(output_dir, output_filename), 'w')

    for graph_filename in sorted(os.listdir(input_dir)):
        # importer le graphe
        g = nx.read_adjlist(os.path.join(input_dir, graph_filename))
        
        # calcul du dominant
        D = sorted(dominant(g), key=lambda x: int(x))

        # ajout au rapport
        output_file.write(graph_filename)
        for node in D:
            output_file.write(' {}'.format(node))
        output_file.write('\n')
        
    output_file.close()
