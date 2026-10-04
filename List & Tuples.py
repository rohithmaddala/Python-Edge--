Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4.5,'python',True,False]
type(a)
<class 'list'>
b=0.9
type(b)
<class 'float'>
c=[0.9]
type(c)
<class 'list'>
a=['python','java','c','c++']
a.append('ml')
a
['python', 'java', 'c', 'c++', 'ml']
a.append('ai','ds')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.append('ai','ds')
TypeError: list.append() takes exactly one argument (2 given)
a.append(['ai','ds'])
a
['python', 'java', 'c', 'c++', 'ml', ['ai', 'ds']]
#extend()
a=['ai','ml','ds']
a.extend(['python','java'])
a
['ai', 'ml', 'ds', 'python', 'java']
#insert()
b=['black','white']
b.insert(1,'red')
b
['black', 'red', 'white']
b.insert(2,'red')
b
['black', 'red', 'red', 'white']
b.insert(0,'red')
b
['red', 'black', 'red', 'red', 'white']
#index()
a=['apple','banana','grapes']
a.index('banana')
1
a.index('grapes')
2
#copy()
a.copy()
['apple', 'banana', 'grapes']
b=a.copy()
b
['apple', 'banana', 'grapes']
#sort()
a=['python','ds','java','ds','ml','ai']
a.sort()
a
['ai', 'ds', 'ds', 'java', 'ml', 'python']
b=[7,3,9,5,6,7,9,11,30,50]
b.sort()
b
[3, 5, 6, 7, 7, 9, 9, 11, 30, 50]
#reverse()
a=['chocolates','ice cream','biryani','KFC']
a.reverse()
a
['KFC', 'biryani', 'ice cream', 'chocolates']
b=[6,8,4,0,1,20]
b.reverse()
b
[20, 1, 0, 4, 8, 6]
#pop()
a=['red','black','white']
a.pop()
'white'
a
['red', 'black']
a.pop('black')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.pop('black')
TypeError: 'str' object cannot be interpreted as an integer
a.pop(1)
'black'
a
['red']
#remove()

a=['red','black','white']
a.remove('red')
a
['black', 'white']
a.remove('black')
a
['white']
a.remove('white')
a
[]
#checking length
a=['hyd,'viz','nlr']
   
SyntaxError: unterminated string literal (detected at line 1)
a=["hyd","viz","nlr"]
   
len(a)
   
3
b='hyd'
   
len(b)
   
3
c=["hyd"]
   
len(c)
   
1
a.count('viz')
   
1
b=['viz','hyd','viz','nlr']
   
b.count('viz')
   
2
#clear
   
>>> a=['monica','harika','harini','geethika']
...    
>>> a.clear()
...    
>>> a
...    
[]
>>> b=[]
...    
>>> b.append('hi')
...    
>>> b
...    
['hi']
>>> #tuple()
...    
>>> a=(3,5.6,'rohith',7+9j,True,False)
...    
>>> type(a)
...    
<class 'tuple'>
>>> #len()
...    
>>> len(a)
...    
6
>>> #count()
...    
>>> a.count()
...    
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> 
>>> a.count(True)
...    
1
>>> a.index(7+9j)
...    
3
