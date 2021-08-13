import unittest
from unittest import result
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card=CardGame()
        self.card1 = Card('hearts', 1)
        self.card2 = Card('clubs', 3)
        self.card3 = Card('spades', 7)
        self.card4 = Card('diamonds', 5)
        self.all_cards = (self.card1, self.card2, self.card3, self.card4)



    def test_check_for_ace(self):
        result = self.card.check_for_ace(self.card1)
        self.assertTrue(result)
        

    def test_highest_card(self):
        result = self.card.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)
        

    def test_cards_total(self):
        result= self.card.cards_total(self.all_cards)
        self.assertEqual('You have a total of ' +str(16), result)
        

    


