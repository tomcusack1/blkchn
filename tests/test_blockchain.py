from blkchn import Blockchain

from unittest import TestCase


class TestBlockchain(TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_add_new_node(self):
        """Tests that adding a new node adds the node successfully to the available nodes set."""
        self.blockchain.register_node(address='0.0.0.0')
        self.assertEqual(self.blockchain.nodes, set('0.0.0.0'))

    def test_new_transaction_id(self):
        """Tests that the new ID on a new blockchain is N+1 from the genesis block."""
        self.assertEqual(self.blockchain.new_transaction({}), 2)
