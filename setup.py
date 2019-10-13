from distutils.core import setup
import setuptools


setup(name='blockchain',
      version='0.0.1',
      author='Tom Cusack-Huang',
      author_email='tom@cusack-huang.com',
      packages=['blockchain'],
      license='MIT',
      url='https://github.com/tomcusack1/blockchain',
      download_url='https://github.com/tomcusack1/blockchain/archive/v_001.tar.gz',
      description='Blockchain data structure',
      install_requires=['flask', 'requests'])
