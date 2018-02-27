# fix_dict: fix your dict and insert it into MongoDB

Removes dots "." from keys, as mongo doesn't like that.
Also, convert ints more than 8-bytes  to string cause BSON can only handle up to 8-bytes ints.
Finaly, your lovely MongoDB can accept your dict and store it.

#  Installation
```
$ pip install fix-dict
```
# Quick Start
```python
>>>from fix_dict import fix_dict
>>>a = {"sen.li":112132312312}
>>>b = fix_dict(a)
>>> b
{'sen_li': '112132312312'}
```
