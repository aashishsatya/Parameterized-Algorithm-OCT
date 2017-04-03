#!/usr/bin/env python
#
# http://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm
# Ford-Fulkerson algorithm computes max flow in a flow network.
#

class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.target = v
    self.capacity = w

  def __repr__(self):
    return "%s->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
  def  __init__(self):
    self.adj = {}
    self.flow = {}

  def AddVertex(self, vertex):
    self.adj[vertex] = []

  def GetEdges(self, v):
    return self.adj[v]

  def AddEdge(self, u, v, w = 0):
    if u == v:
      raise ValueError("u == v")
    edge = Edge(u, v, w)
    redge = Edge(v, u, 0)
    edge.redge = redge
    redge.redge = edge
    self.adj[u].append(edge)
    self.adj[v].append(redge)
    # Intialize all flows to zero
    self.flow[edge] = 0
    self.flow[redge] = 0

  def FindPath(self, source, target, path):
    if source == target:
      return path
    for edge in self.GetEdges(source):
      residual = edge.capacity - self.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = self.FindPath(edge.target, target, path + [(edge, residual)])
        if result != None:
          return result

  def MaxFlow(self, source, target):
    path = self.FindPath(source, target, [])
    print 'path after enter MaxFlow: %s' % path
    for key in self.flow:
      print '%s:%s' % (key,self.flow[key])
    print '-' * 20
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        self.flow[edge] += flow
        self.flow[edge.redge] -= flow
      for key in self.flow:
        print '%s:%s' % (key,self.flow[key])
      path = self.FindPath(source, target, [])
      print 'path inside of while loop: %s' % path
    print "matched vertices:"
    pairs = []
    for key in self.flow:
      if (key.source!=source) and (key.target!=target) and (key.capacity==self.flow[key]) and (key.capacity != 0):
		  print key
		  key_str = str(key)
		  key_str_split = key_str.split('->')
		  left = key_str_split[0]
		  right = key_str_split[1].split(':')[0]
		  pairs.append((left, right))
    return pairs, (sum(self.flow[edge] for edge in self.GetEdges(source)))
	
	
	
if __name__ == "__main__":
	g = FlowNetwork()
	map(g.AddVertex, ['0', '1', '2', '3','4','5','6','7','8','9'])
	g.AddEdge('0','5',1);
	g.AddEdge('0','6',1);
	g.AddEdge('0','8',1);
	g.AddEdge('1','5',1);
	g.AddEdge('1','6',1);
	g.AddEdge('2','5',1);
	g.AddEdge('2','7',1);
	g.AddEdge('2','8',1);
	g.AddEdge('3','6',1);
	g.AddEdge('3','9',1);
	g.AddEdge('4','6',1);
	g.AddEdge('4','9',1);
	
	g.AddVertex('s')
	g.AddVertex('t')
	for u in xrange(0,5):
		g.AddEdge('s',str(u),1)
	for v in xrange(5,10):
		g.AddEdge(str(v),'t',1)
	
	print g.MaxFlow('s', 't')
