from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='article-classifier',
    version='0.1.0',
    description='Classify artivles',
    long_description=readme,
    author='jspc',
    author_email='james@zero-internet.org.uj',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),

    install_requires=[
        "pandas==0.25.3",
        "spacy==2.2.3"
    ]
)
