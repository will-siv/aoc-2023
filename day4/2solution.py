
with open("data.txt", 'r') as r:
  cards = [[1,line[:-1].split(': ')[1]] for line in r]

s = 0
for i, card in enumerate(cards):
  winning_numbers, given_numbers = [[int(y) for y in x.split()] for x in card[1].split(" | ")]
  matches = 0
  for num in winning_numbers:
    if num in given_numbers:
      matches += 1
  for k in range(matches):
    try:
      cards[k + 1 + i][0] += card[0]
    except IndexError:
      continue
  s += card[0]

print(s)
