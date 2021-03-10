# Blkchn [![Build Status](http://178.62.80.42:8081/buildStatus/icon?job=blkchn%2Fdevelop&build=2)](http://178.62.80.42:8081/job/blkchn/job/develop/2/)

A Python implementation of a Blockchain data structure.

# Features

  * Easily integrate into existing code a Blockchain design pattern
  * 100% coverage and extensively tested
  * Tested with Python 3.8
  * Plenty of examples to get you going!

# Installation

You can install the latest version using Pip:

`pip install blkchn`

# Contributing

Pull requests are always welcome to help maintain and improve the codebase.
Please work on your own branch and then raise a PR when ready.

## Releasing to PyPi

The Dockerfile in this project builds using the latest version built.
You should release this first, prior to creating a new instance of the API.
If Jenkins fails, for whatever reason, follow these instructions to release a new version:

First, create the source distribution (ensure you've version bumped `setup.py`):

`python setup.py sdist`

Then upload the new version to PyPi:

`twine upload dist/*`

## Releasing the API to GCP

First, build the Dockerfile and take note of the tag name when complete:

`gcloud builds --project blkchn submit --tag gcr.io/blkchn/blkchn:latest .`

If you don't have a cluster created, then do this now:

```
gcloud container clusters create blkchn-cluster \
    --zone us-west1-a \
    --node-locations us-west1-a \
    --machine-type=e2-small \
    --max-nodes=1 \
    --enable-basic-auth \
    --issue-client-certificate \
    --num-nodes=1
```

Then, once your build has completed, you can apply your Kubernetes yaml to the cluster
to pick up the latest image.

`kubectl apply -f deployment/app.yaml`

`kubectl apply -f deployment/service.yaml`

`kubectl apply -f deployment/ingress.yaml`

Finally, navigate to the external IP outputted by `kubectl get ingress blkchn-ingress`. Some example API
calls are outlined below.

# API Example Usage

Using the API to interact is quite straightforward. Below are some example commands
to demonstrate its usage:

```python
import json
import requests

# Step 1) Add new node to the network
r= requests.post('http://localhost:8080/nodes/register',
                 json={'nodes': ['192.168.1.8:8080']}).json()
print(json.dumps(r, indent=2))

# Step 2) Inspect the empty blockchains genesis block
r = requests.get('http://localhost:8080/chain').json()
print(json.dumps(r, indent=2))

# Step 3) Alice sends Bob 10 of something.
r = requests.post('http://localhost:8080/transactions/new',
                  json={'sender': 'alice',
                        'recipient': 'bob',
                        'amount': 10})

assert r.status_code == 201

# Step 4) Inspect the transaction on the blockchain
r = requests.get('http://localhost:8080/chain').json()
print(json.dumps(r, indent=2))

# Step 5) Mine the block
r = requests.get('http://localhost:8080/mine').json()
print(json.dumps(r, indent=2))
```

# Running Tests

You can run the test suite by running the below command in the root of the module:

`python3 -m unittest`

# License

This project is licensed under the MIT License - see the LICENSE.md file for details