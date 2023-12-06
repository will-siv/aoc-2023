import sys
import threading

maps = []
currMap = []
seedsin = []
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
      seedsin = [int(x) for x in line.split(': ')[1].split()]
    if 'map' in line:
      isMap = True
maps.pop(0)

seedRanges = []
temp = []
i = 0

for seed in seedsin:
  temp.append(seed)
  if i%2 == 1:
    seedRanges.append(temp)
    temp = []
  i += 1


mins = []
# calculates smallest num for a range of seeds
def numCalc(r):
  minNum = ''
  for num in r:
    print(num)
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

  print(f"finished thread {threading.current_thread().name}\
      with result {minNum}")
  mins.append(minNum)

threads = []

for i, rs in enumerate(seedRanges):
  r = range(rs[0], rs[0] + rs[1])
  name = f"t{i}"
  threads.append(threading.Thread(target=numCalc, args=(r,), name=name))

for t in threads:
  t.start()

for t in threads:
  t.join()

print("Done! Below if not printed")
print(min(mins))
