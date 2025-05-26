Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import keyword
>>> all_key = keword.kwlist
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    all_key = keword.kwlist
NameError: name 'keword' is not defined. Did you mean: 'keyword'?
>>> all_key = keyword.kwlist
>>> print(all_key)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(all_key))
35
>>> soft_key=keywordsoftkwlist
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    soft_key=keywordsoftkwlist
NameError: name 'keywordsoftkwlist' is not defined
>>> soft_key=keywordsoft.kwlist
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    soft_key=keywordsoft.kwlist
NameError: name 'keywordsoft' is not defined
>>> soft_key=keyword.softkwlist
>>> print(soft_key)
['_', 'case', 'match', 'type']
>>> print(len(soft_key))
4
>>> import string
>>> spe_sym=string.punctuation
>>> print(spe_sym)
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
>>> print(len(spe_sym))
32
>>> 1x=10
SyntaxError: invalid decimal literal
>>> _x=10
>>> print(_x)
10
>>> true=10
>>> print(true)
10
>>> True=10
SyntaxError: cannot assign to True
