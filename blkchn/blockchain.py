from hashlib import sha256
import json
import requests
from time import time
from urllib.parse import urlparse


class Blockchain:

    def __init__(self):
        """The constructor for the Blockchain class

        Args:
          current_transactions (list): A list of all the pending transactions
          chain (list): A record of all the blocks within the Blockchain
          nodes (set): A unique collection of all connected nodes (e.g. http://192.168.0.5:5000)
          new_block (list): Creates a new Blockchain by making the Genesis Block

        """
        self.current_transactions = list()
        self.chain = list()
        self.nodes = set()
        self.new_block(previous_hash='1', proof=100)  # Genesis Block

    def register_node(self, address):
        """Adds a new node to the list of nodes

        Args:
            address (str): Address of a node. E.g. 'http://192.168.0.5:5000'

        Returns:
            None: If successful, else raises a ValueError

        """

        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')

    def valid_chain(self, chain):
        """Determines if a given blockchain is valid

        Args:
          chain (list): A list of dictionaries (blocks) making up a blockchain

        Returns:
            bool: True if valid, False if not

        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]

            # Check that the hash of the block is correct
            last_block_hash = self.hash(last_block)

            if block['previous_hash'] != last_block_hash:
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """The consensus algorithm

        Resolves conflicts by replacing the chain with the longest one in the network.

        Returns:
            bool: True if our chain was replaced, False if not

        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False

    def new_block(self, proof: int, previous_hash: str) -> dict:
        """Creates a new Block on the Blockchain

        Args:
          proof: The proof given by the Proof of Work algorithm
          previous_hash: Hash of previous Block

        Returns:
          dict: New Block

        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """Creates a new transaction to go into the next mined block

        Args:
          sender (str): Address of the Sender
          recipient (str): Address of the Recipient
          amount (float): Amount

        Returns:
          int: The index of the Block that will hold this transaction

        """
        self.current_transactions.append({'sender': sender, 'recipient': recipient, 'amount': amount})

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        """Returns the last block on the blockchain."""

        return self.chain[-1]

    @staticmethod
    def hash(block: dict) -> str:
        """Creates a SHA-256 hash of a Block

        We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes

        Args:
          block (dict): A single block on the blockchain

        Returns:
          str: A hash of the block

        """
        block_string = json.dumps(block, sort_keys=True).encode()

        return sha256(block_string).hexdigest()

    def proof_of_work(self, last_block) -> int:
        """Proof of Work Algorithm

         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof

        Args:
          last_block (dict): Last Block

        Returns:
          int: The proof of work

        """

        last_proof = last_block['proof']
        last_hash = self.hash(last_block)
        proof = 0

        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int, last_hash: str) -> bool:
        """Validates the Proof

        Args:
          last_proof (int): Previous Proof
          proof (int): Current Proof
          last_hash (int): The hash of the Previous Block

        Returns:
          bool: True if correct, False if not.

        """
        guess = f'{last_proof}{proof}{last_hash}'.encode()

        return sha256(guess).hexdigest()[:4] == '0000'
