import random as rd

class CardDP:
    """
    A card deck for Question 1

    This module consists of a class of cards, from which we can draw individual cards

    The functions in this module are:
        * drawCard
    """

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
        """
        Draws a card from the specified deck

        Returns:
            A randomly selected card
        """
        return [rd.choice(self.suits), rd.choice(self.numbers)]
