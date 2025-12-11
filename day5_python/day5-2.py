FILENAME = "input5.txt"
from collections import defaultdict

with open(FILENAME, 'r') as f:
  lines = f.read().splitlines()
  line = lines[0]
  i = 0
  countMap = defaultdict(int) 

  while line != '':
    begin, end = map(int, line.split('-'))
    countMap[begin] += 1
    countMap[end+1] -= 1
    i += 1
    line = lines[i] 

  count = 0
  prev = -1 
  current = 0
  for key in (sorted(countMap.keys())):
    prev = current
    current += countMap[key]

    if prev == 0:
      prevKey = key
      continue
    
    count += key - prevKey
    prevKey = key

  print(count)
