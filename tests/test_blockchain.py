from blkchn import Blockchain

from unittest import TestCase


class TestBlockchain(TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_add_new_node(self):
        """Tests that adding a new node adds the node successfully to the available nodes set."""
        self.blockchain.register_node(address='0.0.0.0')
        self.assertEqual(self.blockchain.nodes, set('0.0.0.0'))
