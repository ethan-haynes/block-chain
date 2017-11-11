from setuptools import setup, find_packages
import blocks

setup(
   name='blocks',
   version=blocks.__version__,
   description='A block-chain module',
   author=blocks.__author__,
   author_email='ethan@foo.com',
   packages=find_packages(),
   entry_points={
        'console_scripts': [
            'blocks = blocks.__main__:main',
        ],
    }
)
