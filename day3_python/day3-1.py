FILENAME = "input3.txt"
total = 0
with open(FILENAME, 'r') as f:
  lines = f.read().splitlines()

  for line in lines:
    max1 = max(line[:-1])
    max2 = max(line[line.find(max1)+1:])
    total += int(max1 + max2)

  print(total)
