# Blockchain

A Python implementation of a Blockchain, which includes an API whereby
all connected nodes can communicate with one another to mine or
generate concensus over the new blocks to append to the Blockchain.

# Installation

1. Create a new Conda environment

`conda create -n blockchain`

2. Run tests

`python3 -m unittest`

3. Build Conda package

`cd conda-recipe`

`conda build .`

# Running Application

`python3 blockchain.py`

`python3 blockchain.py -p 5001`

`python3 blockchain.py --port 5002`

# Running Tests

Run:

`python3 -m unittest`