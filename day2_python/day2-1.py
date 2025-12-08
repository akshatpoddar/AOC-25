FILENAME = "input2.txt"
total = 0 
with open(FILENAME, 'r') as f:
  ranges = f.read().split(',')
  for my_range in ranges:
    range_str= my_range.split('-')
    begin = int(range_str[0])
    end = int(range_str[1])
    
    for i in range(begin, end+1):
      l = len(str(i))
      for j in range(2, l + 1):
        if l%j == 0 and str(i)[:l//j] * j == str(i):
          total += i 
          break

  print(total) 
