# nested_dict_diff
Return a dict of keys that differ with another config If a value is not found in one fo the configs, it will represented by KEYNOTFOUND

usage
-----
sample scenario
```python
>>> from nested_dict_diff import nested_dict_diff
>>> a = {'a':1, 'b': 2}
>>> b = {'a':2, 'c': 2}
>>> diff = nested_dict_diff(a, b)
>>> print diff
{'a': (1, 2), 'c': 'key not found in first dict', 'b': 'key not found in second dict'}
```

ignore specified keys scenario
```python
>>> from nested_dict_diff import nested_dict_diff
>>> a = {'a': {'b': [{'c': [{'d': [{'e': 1, 'f': 2}]}]}]}}
>>> b = {'a': {'b': [{'c': [{'d': [{'e': 1}]}]}]}}
>>> 
>>> diff = nested_dict_diff(a, b, ['f', ])
>>> print diff
{}
```