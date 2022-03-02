# card class
import random

class Card:
    def __init__(self):
        self.card_value = 0
        self.suit = ''

    def draw_card(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']

        self.card_value = random.randint(1,13)
        self.suit = suits[random.randint(0,3)]


card = Card()
card.draw_card()

print(card.card_value)
