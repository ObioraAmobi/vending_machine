import unittest
from decimal import Decimal

class TestThatStuffWorks(unittest.TestCase):
    def test_this_thing_is_on(self):
        self.assertEquals(give_change(.17), [.10, .02, .05])
        self.assertEqual(give_change(.18), [.10, .05, .02, .01])
        self.assertEqual(give_change(.04), [.02, .02])


coins = [1, .50, .20, .10, .05, .02, .01]

def give_change(amount):
    change = []
    amount = Decimal(str(amount))
    for coin in coins:
        coin = Decimal(str(coin))
        while coin <= amount:
            amount -= coin
            change.append(float(coin))
    return change