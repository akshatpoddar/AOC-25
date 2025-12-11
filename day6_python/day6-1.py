FILENAME = "input6.txt"

with open(FILENAME, 'r') as f:
  lines = f.read().splitlines()
  op = lines[-1].split()
  valMap = [0 if op[i] == '+' else 1 for i in range(len(lines[0].split()))] 

  for i in range(len(lines) - 1):
    words = lines[i].split()
    for j, word in enumerate(words):
      if op[j] == '+':
        valMap[j] += int(word)
      else:
        valMap[j] *= int(word)
  
  
  print(sum(valMap))
