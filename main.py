import random

def randomNumber():
  number = random.randint(1,90)
  return number

bingo = []

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(randomNumber())

bingo = [ [numbers[0], numbers[1], numbers[2]],
        [numbers[3], "BINGO", numbers[4]],
        [numbers[5], numbers[6], numbers[7]] ]

prettyPrint()