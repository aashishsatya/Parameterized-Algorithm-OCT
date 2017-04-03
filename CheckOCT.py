from GraphUtil import *
import sys

graph, k = read_graph(sys.argv[1])
graph_edges = graph.E

vertices = list(graph.V)

if k + 2 > len(vertices):
	print 'Yes instance'
	sys.exit(0)
	
# take a k+2-sized subset

subset = vertices[0: k + 2]

# construct the induced subgraph

new_graph = get_induced_subgraph(graph, set(subset))


		
