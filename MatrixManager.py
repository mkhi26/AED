
import math
class MatrixManager:

    def __init__(self):
        pass

    def getHight(self,n):
        return math.ceil(math.log(n+1,2))
    
    def getWeight(self,h):
        return (int(math.pow(2,h-1))*2-1)
    
    def getMatrixNull(self,n):
        matrix=[]
        h=self.getHight(n)
        w=self.getWeight(h)
        for i in range(h):
            vector=[]
            for j in range(w):
                vector.append(0)
            matrix.append(vector)
        return matrix

    def fillMatrix(self,n):
        matrix=self.getMatrixNull(n)
        h=self.getHight(n)
        EM=math.floor(self.getWeight(h)/2)
        print(EM)
        for i in range(h):
            if i==0:
                matrix [0] [EM] = 1
            middle=EM
            start=math.floor(EM/2)

            if i>0:
                for j in range(start,self.getWeight(h)-start,middle+1):
                    matrix[i][j]=1
                EM=math.floor(EM/2)      
        return matrix




