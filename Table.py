from Heap import*
from MatrixManager import *
class Table:
    def __init__(self, l = []):
        self.l = l
        


    def getMatrixLevels(self):
        heap = Heap()
        n = len(self.l)
        hight = heap.getHight(n)
        width = heap.getWidth(hight)
        matrix = []
        for i in range(hight):
            n = 2**i

            start = n - 1
            end = heap.getWidth(i+1) + start
            matrix.append(self.l[start:end])
        if len(matrix[-1])< width:

            for i in range(width - len(matrix[-1])):
                matrix[-1].append(" ")

        
        return matrix


    def createMatrix(self):
        n = len(self.l)
        matrixLevels = self.getMatrixLevels()
        matrixManager = MatrixManager()
        fillMatrix = matrixManager.fillMatrix(n)
        count = 0
        for i in fillMatrix:

            fillMatrix[count] = self.createRow(i, matrixLevels[count])

            count +=1
        return fillMatrix
            


    def createRow(self, rowNull, level):
 

        count = 0
        for i in range(len(rowNull)):
            if rowNull[i] == 0:
                rowNull[i]= " "
    
            if(rowNull[i]== 1):
                rowNull[i]= level[count] 

                count +=1
                

        return rowNull