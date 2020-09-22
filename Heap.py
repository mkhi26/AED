import math
from NodeHeap import *

class Heap:
    def __init__(self):
        self.root = None

    def getParentIndex(self, childrenIndex):
        parentIndex = (childrenIndex -1)//2
        return parentIndex

    def getChildrenLeftIndex(self, valueParent):
        parentIndex = self.list.getIndex(valueParent)

        return 2 * parentIndex + 1

    def getChildrenRightIndex(self, valueParent):
        parentIndex = self.list.getIndex(valueParent)
        return 2 * parentIndex +2

    def getHight(self, n):
        
        return math.ceil(math.log2(n+1)) 

    def getWidth(self, h):

        return 2**(h-1)





    

            

