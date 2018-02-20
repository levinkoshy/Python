#Implementing a binary tree using lists

#Binary tree : when all the nodes have only 2 children each

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


-----------------------------------------------------------------------
#Implementation of Binary Key using nodes and references

class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


------------------------------------------------------------------------------

#Validation of binary search tree

#if the left node -> root -> right node is sorted, then we can say that the tree is a binary search tree.




-----------------------------------------------------------------------------


import collections

def levelOrderPrint(tree):
    if not tree:
        return
    
    nodes = collections.deque([tree])
    
    currentCount = 1
    nextCount = 0
    
    while len(nodes) != 0:
        
        currentNode = nodes.popleft()
        currentCount -= 1
        
        print(currentNode.val)
        
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount +=1
            
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount +=1
            
        if currentCount == 0:
            print('\n')
            
        currentCount,nextCount = nextCount,currentCount


root = Node(1)

root.left = Node(2)
root.right = Node(3)

levelOrderPrint(root)

------------------------------------------------------------------------
# Trim binary search tree
# Trimming the nodes which are not in between a minimum and maximum value
# we use post order traversal - left,right,root

def trimbst(tree,minVal,maxVal):
    
    if not tree:
        return
    
    tree.left = trimbst(tree.left,minVal,maxVal)
    tree.right = trimbst(tree.right,minVal,maxVal)
    
    if minVal <= tree.val <= maxVal:
        return tree
    
    if tree.val < minVal:
        return tree.right
    
    if tree.val > maxVal:
        return tree.left