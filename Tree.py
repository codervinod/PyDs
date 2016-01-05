'''
implementation of a binary tree
'''

class TreeNode:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def inOrder(self,*args):
        if len(args) <=0:
            node = self.root
        else:
            node = args[0]

        if node is None:
            return

        self.inOrder(node.left)
        print node.item
        self.inOrder(node.right)

def main():
    tree = Tree()
    root = TreeNode(1)
    leftC = TreeNode(3)
    rightC = TreeNode(7)
    tree.root = root
    root.left = leftC
    root.right = rightC
    tree.inOrder()

if __name__=='__main__' : main()



