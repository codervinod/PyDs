#!/usr/bin/python

'''
Basic implementation of Graphs in Python
'''
from collections import deque

class Graph:
    def __init__(self):
        self.nodes = {}

    def addEdge(self,v1,v2):
        print('adding edge %s,%s'%(v1,v2))
        if v1 not in self.nodes:
            self.nodes[v1] = []
        self.nodes[v1].append(v2)

        if v2 not in self.nodes:
            self.nodes[v2] = []
        self.nodes[v2].append(v1)

    def BFS(self):
        print('Traversing BFS')
        q = deque()
        q.append(self.nodes.iterkeys().next())
        visited = []
        while len(q) > 0:
            curr_q = deque(q)
            q.clear()
            for e in curr_q:
                if e not in visited:
                    visited.append(e)
                    print e
                    for n in self.nodes[e]:
                        q.append(n)

    def DFSUtil(self,e,visited):
        if e not in visited:
            visited.append(e)
            print e
            for n in self.nodes[e]:
                self.DFSUtil(n,visited)

    def DFS(self):
        print('Traversing DFS')
        visited = []
        e = self.nodes.iterkeys().next()
        self.DFSUtil(e,visited)

def main():
    g = Graph()
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(4,1)
    g.addEdge(2,4)
    g.addEdge(4,5)

    g.BFS()
    g.DFS()

if __name__=='__main__':main()
