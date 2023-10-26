import random as rd

class CardDP:
    def __init__(self):
        """
            Set up the deck
        """

        # Set up the suits and numbers
        self.suits = ['Spades', 'Clubs', 'Hearts']
        self.numbers = [
            '2',
            '4',
            '5',
            '6',
            '6',
            '7',
            '8',
            '9',
            '10',
            'Queen',
            'King',
            'Ace']
        
    def drawCard(self):
        return [rd.choice(self.suits),rd.choice(self.numbers)]