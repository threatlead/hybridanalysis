from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='hybridanalysis',
    version='0.1',
    description='HybridAnalysis Module',
    long_description=readme,
    author='threatlead',
    author_email='threatlead@gmail.com',
    url='https://github.com/threatlead/',
    license=license,
    packages=find_packages(exclude=('tests',))
)