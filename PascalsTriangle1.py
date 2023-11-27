def PascalsTriangle(numRows):
    triangle = [[1], [1, 1]]
    if numRows == 1 or numRows == 2:
        return triangle[numRows - 1]
    
    while len(triangle) < (numRows):
        lastRow = triangle[-1]
        
        index = 0
        newRow = [1]
        while len(newRow) < len(lastRow):
            num1 = lastRow[index]
            num2 = lastRow[index + 1]
            newRow.append(num1 + num2)
            index += 1
            
        newRow.append(1)
        triangle.append(newRow)
        
    return triangle
            
print(PascalsTriangle(15))