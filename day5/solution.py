import sys

maps = []
currMap = []
seeds = []
isMap = False

with open("data.txt") as r:
  for line in r.read().split('\n'):
    if len(line) == 0:
      isMap = False
      maps.append(currMap)
      currMap = []
    if isMap:
      currMap.append([int(x) for x in line.split()])
    if 'seeds' in line:
      seeds = [int(x) for x in line.split(': ')[1].split()]
    if 'map' in line:
      isMap = True
maps.pop(0)

minNum = ''
for num in seeds:
  # print(num)
  for _map in maps:
    closeMap = _map[0]
    for dst, src, _range in _map:
      # find closest src to num without going over
      if src > num:
        continue
      if closeMap[1] < src or num < closeMap[1]:
        closeMap = [dst, src, _range]
    dst, src, _range = closeMap
    if num >= src and num < src + _range:
      diff = src-dst
      num = num-diff
    else:
      num = num
    # print(f"num is now {num}")
  # print(f"found {num}\n")
  if minNum == '' or num < minNum:
    minNum = num

print(minNum)
