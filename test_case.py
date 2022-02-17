from unittest import TestCase
from main import User

class TestBank(TestCase):

    def test_withdraw(self):
        tom = User("Tom", "tom", "Balance", 20, 1239, 0, 0)
        kalia = User("Kalia", "kalia", "Balance", 0, 6789, 0, 0)
        self.assertEqual(10, tom.withdraw())
        self.assertEqual(0, kalia.withdraw())

    def test_pin_reset(self):
        tom = User("Tom", "tom", "Balance", 20, 1239, 0, 0)
        self.assertEqual(1234, tom.pin_reset())
        self.assertEqual(7, tom.pin_reset())


