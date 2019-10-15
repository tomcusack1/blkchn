# Blkchn

A Python implementation of a Blockchain data structure.

# Installation

`pip install blkchn`

# Release Process

This process will be replaced by Jenkins in the near future.

  1. Increment version numbers in `setup.py`
  2. Create tarball (`python setup.py sdist`)
  3. Add tarball to Git (`git add dist/*`)
  4. Upload package to Pypi (`twine upload dist/*`)
  5. Raise pull request from feature branch into develop
  6. Switch to develop branch and tag release (`git tag -a X.x && git push`)
