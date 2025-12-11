FILENAME = "input6.txt"
from collections import defaultdict

with open(FILENAME, 'r') as f:
  lines = f.read().splitlines()
  cols = list(zip(*lines)) 

  groups = []
  group = [] 
  
  for col in cols:
    if set(col) == {' '}:
      groups.append(group)
      group = [] 
    else:
      group.append(col) 
  groups.append(group)
  total = 0 

  for group in groups:
    op = group[0][-1]
    strings = []
    for elem in group:
      strings.append("".join(elem[:-1]))
    print(strings)
    eval_string = op.join(strings)  
    print(eval_string)
    total += eval(eval_string)

  print(total)
