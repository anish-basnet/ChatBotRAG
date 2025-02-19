
import os

from setuptools import setup, find_packages

_root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_root, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open('HISTORY.md', encoding="utf-8") as f:
    history = f.read()

version = {}
with open(os.path.join(_root, 'ChatBotRAG', 'version.py')) as f:
    exec(f.read(), version)

requirements = []
try:
    with open('requirements.txt', encoding="utf-8") as f:
        requirements = f.read().splitlines()
except IOError as e:
    print(e)

test_requirements = []

setup(
    name='ChatBotRAG',
    version=version['__version__'],
    description='Implementation of simple chatbot',
    long_description=readme + "\n\n" + history,
    author='Anish Basnet',
    author_email='anishbasnetworld@gmail.com',
    url='',
    license='DSDAssist',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='Semantic Features, Similarity, ML, LLM',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10.3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
