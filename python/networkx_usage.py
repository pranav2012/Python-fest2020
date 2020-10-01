import networkx as nx 
import matplotlib.pyplot as plt
 
G = nx.Graph()

G.add_edges_from([(1, 2), (1, 3),(2,3),(2,4),(3,5)])

if nx.is_connected(G):
    print("The Graph is connected")
else:
    print("The Graph has {} connected components".format(nx.number_connected_components(G))) 

print("The shortest path from Node 1 to Node 5 is {}".format(nx.shortest_path(G, source=1, target=5))) #finds the shortest path from source=0 to destination=5

print("The average shortest path is {}".format(nx.average_shortest_path_length(G))) #helps to analyse the average shortest path in the network

plt.figure(figsize=(18,18))
nx.draw_networkx(G, pos=None, arrows=True, with_labels=True) #to draw graph
plt.savefig("Graph.png")
plt.close()
