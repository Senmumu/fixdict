#!/usr/bin/env python
from setuptools import setup

VERSION = '0.1.0'
DESCRIPTION = "fix_dict: fix your dict and insert it into MongoDB"
LONG_DESCRIPTION = """
Removes dots "." from keys, as mongo doesn't like that.

Also, convert ints more than 8-bytes  to string cause BSON can only handle up to 8-bytes ints.

Finaly, your lovely MongoDB can accept your dict and store it.
#  Installation
```
$ pip install fixdict
```
# Quick Start
```python
>>>from fix_dict import fix_dict
>>>a = {"sen.li":112132312312}
>>>b = fix_dict(a)
>>> b
{'sen_li': '112132312312'}
"""

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython',
]

setup(
    name="fix_dict",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    keywords=('dict',
              'python',
              'mongodb',
              'data srtucture',
              'transform',
              'fix',
              'fix dict',
              'remove dot'),
    author="Ryan Luo",
    author_email="luo_senmu@163.com",
    url="https://github.com/Senmumu/fix_dict",
    license="MIT License",
    platforms=['any'],
    test_suite="",
    zip_safe=True,
    install_requires=[],
    packages=['fix_dict']
)
