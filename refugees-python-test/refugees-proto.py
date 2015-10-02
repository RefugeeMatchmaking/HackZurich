import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

B = nx.bipartite_random_graph(30, 10, 0.5)
X, Y =  bipartite.sets(B) # select all refugees
 # all locals 

pos = dict()
pos.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2

pos = nx.spring_layout(B)
nx.draw_networkx_nodes(B, pos=pos, nodelist=X, node_color = 'r')
nx.draw_networkx_nodes(B, pos=pos, nodelist=Y, node_color = 'b')
nx.draw_networkx_edges(B, pos)
plt.show()



