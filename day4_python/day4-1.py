FILENAME = "input4.txt"
count = 0

def hasEnoughAdjacent(lines, i, j):
  dir_i = [0,0,1,-1,1,1,-1,-1]
  dir_j = [1,-1,0,0,1,-1,1,-1]
  m = len(lines)
  n = len(lines[0])
  count = 0
  for k in range(8):
    final_dir_i = dir_i[k] + i
    final_dir_j = dir_j[k] + j
    if (final_dir_i < 0 or final_dir_j < 0 or final_dir_i >=m or final_dir_j >=n):
      continue
    if lines[final_dir_i][final_dir_j] == '@':
      count += 1

  return count<4 

with open(FILENAME, 'r') as f:
  lines = f.read().splitlines()
  m = len(lines)
  n = len(lines[0])
  for i in range(m):
    for j in range(n):
      if lines[i][j] == '@' and hasEnoughAdjacent(lines, i, j):
        count += 1

print(count)
