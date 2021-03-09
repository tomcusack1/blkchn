from blkchn import Blockchain

from unittest import TestCase


class TestBlockchain(TestCase):
    def setUp(self):
        self.blockchain = Blockchain()
