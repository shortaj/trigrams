"""Creating a package"""

from setuptools import setup

dependencies = ['ipython', 'pytest', 'pytest-watch']

setup(
    name='trigrams',
    description='Implements the Trigrams algorithm.',
    version='0.5',
    author='Miguel Pena and Alex Short',
    author_email='miguelp1986@gmail.com',
    py_modules=['trigrams'],
    package_dir={'': 'src'},
    install_requires=dependencies,
    entry_points={'console_scripts': ['trigrams = trigrams:main']}
)