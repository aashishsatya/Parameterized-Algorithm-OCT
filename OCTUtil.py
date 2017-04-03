import itertools
from GraphUtil import *
from FordFulkerson import *

def compression(G, S_dash, k):
	
	for i in xrange(0, len(S_dash) + 1):
		#print i
		for T in itertools.combinations(S_dash, i):
			#print 'ss1 -->', T
			remaining_sets = S_dash - set(T)
			for j in xrange(0, len(remaining_sets) + 1):
				for L in itertools.combinations(remaining_sets, j):
					R = remaining_sets - set(L)
					
					G_l = get_induced_subgraph(G, L)
					bad_guess = 0
					for vertex in G_l.V:
						if len(G_l.E[vertex]) > 0:
							bad_guess = 1
							break
					if bad_guess:
						continue
						
					G_r = get_induced_subgraph(G, R)
					bad_guess = 0
					for vertex in G_r.V:
						if len(G_r.E[vertex]) > 0:
							bad_guess = 1
							break
					if bad_guess:
						continue
					
					G_minus_S_dash = get_induced_subgraph(G, G.V - S_dash)
					# get the bi-partite partitioning of G - S'
					A, B = get_bipartite_partition(G_minus_S_dash)
					A_l = set([])
					A_r = set([])
					B_l = set([])
					B_r = set([])
					for start in L:
						for end in A:
							if end in G.E[start]:
								A_l.add(end)
					for start in L:
						for end in B:
							if end in G.E[start]:
								B_l.add(end)
					for start in R:
						for end in A:
							if end in G.E[start]:
								A_r.add(end)
					for start in R:
						for end in B:
							if end in G.E[start]:
								B_r.add(end)
					Al_union_Br = A_l + B_r
					Ar_union_Bl = A_r + B_l
					G_tilde = UndirectedGraph(G_minus_S_dash.V, G_minus_S_dash.E)
					for start in A_l:
						for end in B_r:
							if end in G_tilde.E[start]:
								G_tilde.E[start].remove(end)
								G_tilde.E[end].remove(start)
					for start in A_r:
						for end in B_l:
							if end in G_tilde.E[start]:
								G_tilde.E[start].remove(end)
								G_tilde.E[end].remove(start)
					G_tilde.V.add('s')
					G_tilde.E['s'] = []
					for start in Al_union_Br:
						G_tilde.E['s'].append(start)
						G_tilde.E[start].append('s')
					G_tilde.V.add('t')
					G_tilde.E['t'] = []
					for start in Ar_union_Bl:
						G_tilde.E['t'].append(start)
						G_tilde.E[start].append('t')
							
					g = FlowNetwork()
					map(g.AddVertex, list(G_tilde.V))
					for start in G_tilde.E:
						for end in G_tilde.E[start]:
							g.addEdge(start, end, 1)
							G_tilde.E[end].remove(start)
							
					if g.MaxFlow('s', 't') <= k - len(T):
						return True
						
	return False

