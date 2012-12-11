from setuptools import setup

with open('README') as f:
    long_description = f.read()

setup(
    name='flat',
    author='Lucian Branescu Mihaila',
    version='0.1',
    license='MIT',
    description='Flattening and unflattening utils.',
    long_description=long_description,
    py_modules='flat',
)