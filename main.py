from MatrixManager import *
from Table import *
from HTMLTable import *

mm = MatrixManager()
l = [110,98,85,58,17,27,78,12,34]

table = Table(l)
matrixTable = table.createMatrix()

html = HTMLTable()
html.createTable(matrixTable)