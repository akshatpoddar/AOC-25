FILENAME = "input5.txt"

with open(FILENAME, 'r') as f:
  lines = f.read().splitlines()
  line = lines[0]
  i = 0
  ranges = []
  while line != '':
    begin, end = line.split('-')
    ranges.append((int(begin),int(end))) 
    i += 1
    line = lines[i] 
  i += 1
  count = 0 
  n = len(lines)
  while i < n:
    x = int(lines[i])
    for begin, end in ranges:
      if x >= begin and x <= end:
        count += 1
        break
    i += 1

print(count)

