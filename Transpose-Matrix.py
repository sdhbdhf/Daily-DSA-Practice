class Solution(object):
    def transpose(self, matrix):
        row=len(matrix)
        column=len(matrix[0])
        temp=[[0]*row for x in range(column)]
        for i in range(column):
            for j in range(row):
                temp[i][j]=matrix[j][i]
        return temp
