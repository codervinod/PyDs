#!/usr/bin/python

'''
Implement basic trie using python dicts
'''

class TrieNode():
    def __init__(self):
        self.endsHere = False
        self.tdict = {}

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

    def exists(self,tstr):
        curr = self._root
        for t in tstr:
            if t not in curr.tdict:
                return False
            curr = curr.tdict[t]
        return curr.endsHere

def main():
    t1 = Trie()
    t1.insert('vinod')
    e = t1.exists('gupta')
    print e



if __name__=='__main__': main()
