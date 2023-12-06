
def numFromArray(a):
  num = 0
  mult = 1
  while len(a) > 0:
    num += a.pop(-1) * mult
    mult *= 10

  print(f"adding {num}\n")
  return num

grid = []
with open("data.txt", 'r') as r:
  for line in r:
    grid.append(line)

length = len(grid[0])
height = len(grid)

# print(length, height)

s = 0
for i in range(height):
  numArray = []
  isPart = False
  for j in range(length):
    try:
      char = int(grid[i][j])
    except ValueError:
      if isPart:
        isPart = False
        num = numFromArray(numArray)
        s += num
      numArray = []
      continue
    numArray.append(char)
    print(f"added {char} to array: {numArray}")
    # check surrounded
    if isPart:
      continue
    for k in range(9):
      try:
        i_off = k//3 - 1 + i
        j_off = k%3 - 1 + j
        test = grid[i_off][j_off]
      except IndexError:
        continue
      if i_off < 0 or j_off < 0:
        continue
      if not ('.' == test or '\n' == test or test.isnumeric()): 
        print(f"[{i_off}, {j_off}] ({test}) makes isPart True")
        isPart = True
        break

print(s)
