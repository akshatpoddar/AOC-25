FILENAME = "input7.txt"

with open(FILENAME, 'r') as f:
  lines = f.read().splitlines()
  m = len(lines)
  n = len(lines[0])
  startInd = n//2
  memo = {} 

  def countSplit(i, j):
    if i >= m:
      return 1
    if j < 0 or j >= n:
      return 0
    if (i,j) in memo:
      return memo[(i,j)]

    if lines[i][j] == '^':
      memo[(i,j)] = countSplit(i, j-1) + countSplit(i, j+1)
      return memo[(i,j)]

    return countSplit(i + 1, j)

  total = countSplit(0, startInd)
  print(total)
