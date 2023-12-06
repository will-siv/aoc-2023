
with open("data.txt", 'r') as r:
  cards = [line.split(': ')[1] for line in r]

s = 0
for card in cards:
  winning_numbers, given_numbers = [[int(y) for y in x.split()] for x in card.split(" | ")]
  score = -1
  for num in winning_numbers:
    if num in given_numbers:
      score += 1
  if score < 0:
    continue
  score = 2**score
  s += score
  print(score)
print(s)
