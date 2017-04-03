# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:25:31 2017

@author: aashishsatya

A script having a set of simple functions to check graph properties.

"""

class UndirectedGraph:
    
    def __init__(self, V, E):
        
        """
        Initialize the Graph class. Accepts a set of vertices V and edges E as input.
        V is implemented as a set
        E is implemented as an adjacency list in the form of a dictionary.
        """
        
        self.V = V
        self.E = E
        
    def __str__(self):
        
        graph_str = ''
        
        for start in self.E.keys():
            for stop in self.E[start]:
                graph_str += start + ' ' + stop + '\n'
                
        return graph_str

def read_graph(file_name):

    E = {}
    V = set([])
    
    input_file = open(file_name, 'r')
    k = int(input_file.readline())
    
    for line in input_file.readlines():
        line = line[:-1]    # remove '\n'
        edge_list = line.split(' ')
        if len(edge_list) == 2:
            # it's a proper edge, not an isolated vertex
            start = edge_list[0]
            end = edge_list[1]
            if start in E:
                # append end to the adjacency list of start
                E[start].append(end)
            else:
                E[start] = [end]
            # ditto for end
            if end in E:
                E[end].append(start)
            else:
                E[end] = [start]
            # add start and end to vertices of the graph
            # since V is a set, duplicates will be taken care of automatically
            V.add(start)
            V.add(end)
        elif len(edge_list) == 1:
            # degree zero vertices
            # their edge set will be []
            vertex = edge_list[0]
            E[vertex] = []
            V.add(vertex)
            
    input_file.close()
    G = UndirectedGraph(V, E)
    return (G, k)
    
def get_induced_subgraph(graph, subset):
	
	"""
	graph is an object of type UndirectedGraph
	subset is a set
	"""
	
	graph_edges = graph.E
	vertices = list(graph.V)

	# construct the induced subgraph

	new_graph_edge = {}
	new_graph_vertices = subset

	for start in graph_edges.keys():
		if start in new_graph_vertices:
			for stop in graph_edges[start]:
				if stop in new_graph_vertices:
					# add it to new_graph_edge
					if start in new_graph_edge:
						new_graph_edge[start].append(stop)
					else:
						new_graph_edge[start] = [stop]

	#print new_graph_vertices					
	#print new_graph_edge
	return UndirectedGraph(new_graph_vertices, new_graph_edge)
