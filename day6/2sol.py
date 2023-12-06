import math

def zs(t, d):
  det = math.sqrt(t*t - (4*d))
  root1 = t/2 - det/2
  root2 = t/2 + det/2
  if root1==int(root1):
    root1 += 1
  return root1, root2

with open('data.txt', 'r') as r:
  times, distances = [[y for y in x.split(":")[1].split()] for x in r.read().split('\n')[:-1]]

times = int("".join(times))
distances = int("".join(distances))
races = [(times, distances)]

vals = [abs(int(r1)-int(r2)) for r1, r2 in [zs(t, d) for t, d in races]]

mult = 1

for val in vals:
  mult *= val

[print(zs(t,d)) for t,d in races]
print(mult)
print(vals)
