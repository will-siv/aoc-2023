# only 12 red cubes, 13 green cubes, and 14 blue cubes

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

def possibleGames(line):
  line = line[:-1]
  game, data = line.split(": ")
  pulls = data.split("; ")
  ballset = [x.split(", ") for x in pulls]
  gameID = int(game.split()[1])

  for balls in ballset:
    for ball in balls:
      num = int(ball.split()[0])
      if 'blue' in ball:
        if num > 14:
          return 0
      if 'green' in ball:
        if num > 13:
          return 0
      if 'red' in ball:
        if num > 12:
          return 0
  return gameID

# power of minimum cubes to play game
# power: numbers in a set multiplied together

def powerPossible(line):
  line = line[:-1]
  game, data = line.split(": ")
  pulls = data.split("; ")
  ballset = [x.split(", ") for x in pulls]

  maxRGB = [0,0,0]
  for balls in ballset:
    for ball in balls:
      num = int(ball.split()[0])
      if 'red' in ball:
        if maxRGB[0] < num:
          maxRGB[0] = num
      if 'blue' in ball:
        if maxRGB[1] < num:
          maxRGB[1] = num
      if 'green' in ball:
        if maxRGB[2] < num:
          maxRGB[2] = num
  return maxRGB[0]*maxRGB[1]*maxRGB[2]

with open("data.txt", 'r') as r:
  print(sum([powerPossible(line) for line in r]))
