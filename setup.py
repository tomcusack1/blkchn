from distutils.core import setup
import setuptools


setup(name='blkchn',
      version='0.0.3',
      author='Tom Cusack-Huang',
      author_email='tom@cusack-huang.com',
      packages=['blkchn'],
      license='MIT',
      url='https://github.com/tomcusack1/blkchn',
      download_url='https://github.com/tomcusack1/blkchn/dist/blkchn-0.0.3.tar.gz',
      description='Blockchain data structure',
      install_requires=['flask', 'requests'])
