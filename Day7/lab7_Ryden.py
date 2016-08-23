"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes 

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 

def make_net(rows = None, cols = None, square_length = None):
  if square_length is not None:
    rows = math.sqrt(square_length)
    cols = rows
  net = {}
  for row in range(1,rows+1):
    for i in range(((row-1)*cols)+1,row*cols):
      net = makeLink(net, i, i+1)
    for i in range(1, rows*cols-cols+1):
      net = makeLink(net, i, i+cols)
  return net


square = make_net(16,16)

# TODO: define a function countEdges

import math

def countEdges(network, rows = None, cols = None):
  if rows is None:
    rows = math.sqrt(len(network))
    cols = rows
  edges = (cols * (rows-1)) + (rows * (cols-1))
  return edges

countEdges(square)


# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

# How many nodes in movies?

len(movies) # 7

# How many edges in movies?

actors = movies.keys()
counted = []
unique = []
for actor in actors:
  unique.extend(filter(lambda x: x not in counted, movies[actor]))
  counted.append(actor)
len(unique) # 10

def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

# TODO: find an Eulerian tour of the movie network and check it 

def findEulerian(graph, path=[]):
  All_Combos = []
  Actors = graph.keys()
  for actor in Actors:
    Others = list(Actors)
    Others.remove(actor)
    for other in Others:
      All_Combos.append(findAllPaths(graph, actor, other))
  indices = []
  for combo in All_Combos:
    for subcombo in combo:
      if len(subcombo) == len(graph.keys()):
        indices.append(subcombo)
  return indices

  return All_Combos
  indices=[]
  for item in All_Combos:
    if len(item) == len(graph.keys()):
      indices.append(item)
  return indices

movie_tour = [] 
tour(movies, movie_tour)


def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

print findPath(movies, jr, ms)


# TODO: implement findShortestPath()
def findShortestPath(graph, start, end, path=[]):
  All = findAllPaths(graph, start, end, [], [])
  indices=[]
  for item in All:
    if len(item) == min([len(i) for i in All]):
      indices.append(item)
  return indices


print findShortestPath(movies, jr, ms)
# print findShortestPath(movies, ms, ss)

# TODO: implement findAllPaths() to find all paths between two nodes


def findAllPaths(graph, start, end, path=[], paths=[]):
        path = path + [start]
        if start == end:
            paths.append(path)
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findAllPaths(graph, node, end, path, paths)
        return paths

allPaths = findAllPaths(movies, jr, ms)
for path in allPaths:
  print path

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.