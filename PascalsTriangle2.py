# Recursive approach

def PascalsTriangle2(numRows):
    # Step 1: Base Cases
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
        
    # Step 2: Recursive Case
    prevRows = PascalsTriangle2(numRows - 1)
    newRow = [1] * numRows
    
    for i in range(1, numRows - 1):
        newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
    
    prevRows.append(newRow)
    return prevRows
            
print(PascalsTriangle2(30))