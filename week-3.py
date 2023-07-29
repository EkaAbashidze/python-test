from random import choice
from random import randint
from random import shuffle

coin = random.choice(["heads", "tails"])

print(randint(1, 10))

cards = ["jack", "queen", "king"]
shuffle(cards)

for card in cards:
    print(card)