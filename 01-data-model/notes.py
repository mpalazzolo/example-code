from .frenchdeck import FrenchDeck
from random import choice
from .vector2d import Vector

# FRENCH DECK EXAMPLE #

deck = FrenchDeck()
len(deck)  # 52

# You don't need to implement a method to pick a random card because python has one
# It utilizes the __getitem__ special method
choice(deck)

# Slicing and other list methods use __getitem__ as well, so no need to implement anything
aces = deck[12::13]

# Rank cards
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
     print(card)


# Right now, this deck cannot be shuffled because it is immutable
# Need to implement __setitem__ for shuffling


# VECTOR EXAMPLE
v1 = Vector(2, 4)
v2 = Vector(2, 1)
v1 + v2

v = Vector(3, 4)
abs(v)

v * 3
abs(v * 3)