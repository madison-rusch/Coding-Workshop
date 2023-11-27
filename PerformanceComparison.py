import time
from PascalsTriangle1 import PascalsTriangle1
from PascalsTriangle2 import PascalsTriangle2
from PascalsTriangle3 import PascalsTriangle3

numRows = 600
  
start1 = time.time()            
PascalsTriangle1(numRows)
end1 = time.time()
print(f'Brute force took {end1-start1} time')

start2 = time.time()
PascalsTriangle2(numRows)
end2 = time.time()
print(f'Recursion took {end2-start2} time')

start3 = time.time()
PascalsTriangle3(numRows)
end3 = time.time()
print(f'Dynamic Programming took {end3-start3} time')
