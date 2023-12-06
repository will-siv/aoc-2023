
def numFromArray(a):
  num = 0
  mult = 1
  while len(a) > 0:
    num += a.pop(-1) * mult
    mult *= 10

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
  for j in range(length):
    # find star, find numbers around, multiply and add if ==2
    if grid[i][j] != '*':
      continue
    # star is found, look for numbers
    power = []
    for k in range(9):
      try:
        i_off = k//3 - 1 + i
        j_off = k%3 - 1 + j
      except IndexError:
        continue
      char = grid[i_off][j_off]
      # find beginning of number, replace data
      if char.isnumeric():
        numArray = []
        strArray = list(grid[i_off])
        start = j_off
        while strArray[start-1].isnumeric():
          start -= 1
        while strArray[start].isnumeric():
          numArray.append(int(strArray[start]))
          strArray[start] = '.'
          start += 1
        grid[i_off] = "".join(strArray)
        power.append(numFromArray(numArray))
    if len(power) == 2:
      print(f"found {power[0]} and {power[1]} in [{i}, {j}]")
      s += power[0] * power[1]

print(s)
