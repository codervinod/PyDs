#!/usr/bin/python

'''
Implement basic trie using python dicts
'''

class TrieNode():
    def __init__(self):
        self.endsHere = False
        self.tdict = {}
        self.str = ''

class Trie():
    def __init__(self):
        self._root = TrieNode()

    def insert(self,tstr):
        curr = self._root
        for t in tstr:
            if t not in curr.tdict:
                curr.tdict[t] = TrieNode()
            curr = curr.tdict[t]
        curr.endsHere = True
        curr.str = tstr

    def exists(self,tstr):
        curr = self._root
        for t in tstr:
            if t not in curr.tdict:
                return False
            curr = curr.tdict[t]
        return curr.endsHere

    def traverse(self,currDict,preList):
        if currDict.endsHere:
            preList.append(currDict.str)

        for k,node in currDict.tdict.iteritems():
            self.traverse(node,preList)

    def startsWith(self,pre):
        curr = self._root
        prelist = []
        for t in pre:
            curr = curr.tdict[t]

        self.traverse(curr,prelist)
        return prelist


def main():
    t1 = Trie()
    t1.insert('vinod')
    t1.insert('app')
    t1.insert('apogy')
    t1.insert('apple')
    t1.insert('appleboy')
    t1.insert('ap')
    t1.insert('axxx')
    e = t1.exists('gupta')
    print e
    prel = t1.startsWith('ap')
    for p in prel:
        print p


if __name__=='__main__': main()
