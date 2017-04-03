import itertools
from GraphUtil import *

def compression(G, S_dash, k):
	
	for i in xrange(0, len(S_dash) + 1):
		#print i
		for T in itertools.combinations(S_dash, i):
			#print 'ss1 -->', T
			remaining_sets = S_dash - set(T)
			for j in xrange(0, len(remaining_sets) + 1):
				for L in itertools.combinations(remaining_sets, j):
					R = remaining_sets - set(L)
					G_minus_S_dash = get_induced_subgraph(G, G.V - S_dash)
					# get the bi-partite partitioning of G - S'
					

