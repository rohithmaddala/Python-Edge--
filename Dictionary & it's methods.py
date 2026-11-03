Python 3.13.15 (tags/v3.13.15:4061bc4, Aug  5 2026, 13:05:39) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary{}
a={'name':'rohith','month':11,'year':2026}
type(a)
<class 'dict'>
b={'year',2026,'month':11,'date':1}
SyntaxError: invalid syntax
b={'year':2026,'month':11,'date':1}
b.keys()
dict_keys(['year', 'month', 'date'])
b.values()
dict_values([2026, 11, 1])
b.items()
dict_items([('year', 2026), ('month', 11), ('date', 1)])
#accessing:
a['year']
2026
a['month']
11
a['name']
'rohith'
b['date']
1
#get()
a.get('name')
'rohith'
a.get('month')
11
a.get('year')
2026
a.get(11)
a
{'name': 'rohith', 'month': 11, 'year': 2026}
a.get(2026)
a
{'name': 'rohith', 'month': 11, 'year': 2026}
b.get('year')
2026
b.get('month')
11
b.get('date')
1
b.get(1)
b
{'year': 2026, 'month': 11, 'date': 1}
c={'name':'rohith','city':'NLR'}
c.update({'year':2026})
c
{'name': 'rohith', 'city': 'NLR', 'year': 2026}
c.update({'month':11,'date':1})
c
{'name': 'rohith', 'city': 'NLR', 'year': 2026, 'month': 11, 'date': 1}
#update()
#setdefault()
d={'hour':9,'min':38}
d.setdefault('sec',10)
10
d
{'hour': 9, 'min': 38, 'sec': 10}
e={'city','NLR','state':'AP','country':'IND'}
SyntaxError: invalid syntax
e={'city':'NLR','state':'AP','country':'IND'}
e
{'city': 'NLR', 'state': 'AP', 'country': 'IND'}
e.pop()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    e.pop()
TypeError: pop expected at least 1 argument, got 0
e.pop('city')
'NLR'
e
{'state': 'AP', 'country': 'IND'}
e.popitem()
('country', 'IND')
e
{'state': 'AP'}
f={'colour':'RED','food':'BIRYANI'}
f.copy()
{'colour': 'RED', 'food': 'BIRYANI'}
g=f.copy()
g
{'colour': 'RED', 'food': 'BIRYANI'}
f.copy(g)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    f.copy(g)
TypeError: dict.copy() takes no arguments (1 given)
f.clear()
>>> f
{}
>>> len(f)
0
>>> len(g)
2
>>> a={'name':'rohith','year':2026,'name':'rohith'}
>>> a
{'name': 'rohith', 'year': 2026}
>>> b={'name':'rohith','year':2026,'name':'rohit'}
>>> b
{'name': 'rohit', 'year': 2026}
>>> c={'name1':'rohith','name2':'rohith','year':2026}
>>> c
{'name1': 'rohith', 'name2': 'rohith', 'year': 2026}
>>> d={'idno.s':{10,20,30],'names':'['rohith','rohit','rohi']}
...    
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> d={'idno.s':{[10,20,30],'names':['rohith','rohit','rohi']}
...    
SyntaxError: invalid syntax
>>>  d={'idno.s':[10,20,30],'names':['rohith','rohit','rohi']
...     
SyntaxError: unexpected indent
>>> d={'idno.s':[10,20,30],'names':['rohith','rohit','rohi']}
...     
>>> d
...     
{'idno.s': [10, 20, 30], 'names': ['rohith', 'rohit', 'rohi']}
>>> type(d)
...     
<class 'dict'>
>>> d.keys()
...     
dict_keys(['idno.s', 'names'])
>>> d.values()
...     
dict_values([[10, 20, 30], ['rohith', 'rohit', 'rohi']])
>>> d.items()
...     
dict_items([('idno.s', [10, 20, 30]), ('names', ['rohith', 'rohit', 'rohi'])])
