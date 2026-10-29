Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a={3,5.6,"rohith",8+9j,True,False}
print(a)
{False, True, 3, (8+9j), 5.6, 'rohith'}
type(a)
<class 'set'>
b={5,6,4,5,6,7,8,9}
print(b)
{4, 5, 6, 7, 8, 9}
#add()
c={2,3,4,5)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
c={1,3,5,7}
c.add(10)
print(c)
{1, 3, 5, 7, 10}
a={2,3,4,5,6,7,8}
b={5,6,7,8}
a.issubset(b)
False
b.issubset(a)
True
a={3,4,5,6,7,8}
b={6,7,8}
a.issuperset(b)
True
b.issuperset(a)
False
#union()
a={1,2,3,4,5,6}
b={4,5,6,7,8}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
b.union(a)
{1, 2, 3, 4, 5, 6, 7, 8}
#intersection()
a={3,4,5,6,78,8,9}
b={6,7,8,9,10}
a.intersection(b)
{8, 9, 6}
b.intersection(a)
{8, 9, 6}
a={10,11,12,13,14,15}
b={13,14,15,16,17}
a.difference(b)
{10, 11, 12}
a={10,20,30,40,50}
b={30,40,50,60,70}
a.update(b)
a
{70, 40, 10, 50, 20, 60, 30}
b
{50, 70, 40, 60, 30}
a
{70, 40, 10, 50, 20, 60, 30}
b.update(a)
b
{70, 40, 10, 50, 20, 60, 30}
a.update(a)
a
{70, 40, 10, 50, 20, 60, 30}
a={2,3,4,5,6,7}
b={4,5,6,7,8,9}
a.symmetric_difference(b)
{2, 3, 8, 9}
c={4,5,6,4,5,6,7}
d={4,5,3,1,2,7,8,9,10}
c.symmetric_difference(d)
{1, 2, 3, 6, 8, 9, 10}
a={3,4,5,6,7,8}
b={7,8,9,10}
a.difference_update(b)
a
{3, 4, 5, 6}
b.difference_update(a)
b
{8, 9, 10, 7}
a={3,4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection_update(a)
a.intersection_update(b)
a
{8, 9, 6, 7}
b.intersection_update(a)
b
{8, 9, 6, 7}
a={3,4,5,6,7}
b=5,6,7,8,9}
SyntaxError: unmatched '}'
b={5,6,7,8,9}
a.symmetric_difference_update(b)
a
{3, 4, 8, 9}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7}
a={6,7,8,9,10}
>>> b={8,9,10,11,12}
>>> a.copy()
{6, 7, 8, 9, 10}
>>> b=a.copy()
>>> b
{6, 7, 8, 9, 10}
>>> a.pop()
6
>>> a.pop(9)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.pop(9)
TypeError: set.pop() takes no arguments (1 given)
>>> b.pop()
6
]
>>> a.remove(10)
>>> a
{7, 8, 9}
>>> b.remove(9)
>>> b
{7, 8, 10}
>>> a={5,6,7,8}
>>> a.discard(7)
>>> a
{8, 5, 6}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(20)
>>> b
{20}
>>> a={1,2,3,4,5,}
>>> b={6,7,8,910}
>>> a.isdisjoint(b)
True
>>> len(a)
5
>>> len(b)
4
