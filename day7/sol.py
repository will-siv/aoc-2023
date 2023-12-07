import json

def clearEmpty(b):
  keys = b.keys()
  for item in keys:
    if b[item] == 0:
      print(b.pop(item))

with open("small.txt") as r:
  for line in r:
    lines = r.read().split('\n')[:-1]

scores = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
    ]

defCardBin = 'akqjt98765432'
cardMap = {
    't': '10',
    'j': '11',
    'q': '12',
    'k': '13',
    'a': '14',
    }
for line in lines:
  cardbin = {}
  cards, bid = line.split()
  for card in cards:
    try:
      int(card)
    except:
      card = cardMap[card.lower()]
    try:
      cardbin[card] += 1
    except:
      cardbin[card] = 1

  full = False
  high = False
  binned = False
  for card in cardbin:
    try:
      int(card)
    except:
      card = cardMap[card]
    # insert into scores value
    if cardbin[card] == 5:
      scores[0].append((cardbin.copy(), bid))
    if cardbin[card] == 4:
      scores[1].append((cardbin.copy(), bid))
      binned = True
    if cardbin[card] == 3:
      if full:
        scores[2].append((cardbin.copy(), bid))
        scores[4].pop(-1)
      else:
        scores[3].append((cardbin.copy(), bid))
        binned = True
    if cardbin[card] == 2:
      if full:
        scores[2].append((cardbin.copy(), bid))
        scores[3].pop(-1)
      elif not binned:
        scores[4].append((cardbin.copy(), bid))
        binned = True
      else:
        scores[4].pop(-1)
        scores[5].append((cardbin.copy(), bid))
  if not binned:
    scores[6]
# working 

scoresArray = []
for board in scores:
  boardArray = []
  for hand, bet in board:
    temp = []
    for key in hand:
      for i in range(hand[key]):
        temp.append(key)
    temp.sort(key=lambda x: int(x))
    temp.reverse()
    boardArray.append((temp, bet))
  scoresArray.append(boardArray)

# this doesn't work - leaving to tomorrow :(
