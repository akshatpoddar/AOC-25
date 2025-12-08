FILENAME = "input1.txt"

pos = 50
count = 0
with open(FILENAME, 'r') as f:
  lines = f.read().splitlines()
  for line in lines:
    dir = 1 if line[0] == 'R' else -1
    num = int(line[1:])
    
    oldPos = pos
    pos = pos + dir*num

    count += abs(pos) // 100
    
    if dir < 0 and oldPos != 0 and pos <= 0:
      count += 1 

    pos = pos % 100



print(count)


  
