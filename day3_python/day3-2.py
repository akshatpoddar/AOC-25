FILENAME = "input3.txt"
total = 0
with open(FILENAME, 'r') as f:
  lines = f.read().splitlines()
  
  for line in lines:
    n = len(line)
    maxPos = -1 
    current = ""
    for i in range(12,0,-1):
      max1 = max(line[maxPos+1: n-(i-1)])
      maxPos = line.index(max1, maxPos + 1)
      current += max1
    total += int(current)

  print(total)
