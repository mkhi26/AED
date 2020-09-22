#-*-coding: utf-8 -*-
class HTMLTable:
    def __init__(self):
        pass


    def getTable(self, matrix):
        content = '<!DOCTYPE html><html><head><style>body{background-color:rgb(195, 239, 226);}table,td{background-color: rgb(37, 141, 110);border:1px solid rgb(195, 239, 226);color:White};</style></head>'
        for i in matrix:
            content += self.getRowTable(i)
        
        return "<table border = '1'>%s</table></html>"%content 


    def getRowTable(self, row):
        
        for i in range(len(row)):
            # <td><tr></tr>
            row[i]= "<td width='24.37' height='23'>%s</td>"% row[i]
        return "<tr>%s</tr>"% " ".join(row)


    def createTable(self, matrix):
        content = self.getTable(matrix)
        f = open("HEAPHtml.html","w")
        f.write(content)
        f.close()
        return True