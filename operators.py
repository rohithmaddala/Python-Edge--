Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arithematic
a=3
b=6
print(a+b)
9
print(a-b)
-3
print(a*b)
18
print(a//b)
0
print(a/b)
0.5
print(a**b)
729
#Assignment
a=3
b=4
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
7
a-=1
a
6
a*=5
a
30
a//=2
a
15
a**=2
a
225
a%=4
a
1
b+=a
b
5
b-=1
b
4
b*=5
b
20
b//=2
b
10
b**=2
b
100
b%=4
b
0
#Comparison
a=4
b=8
a>b
False
a<b
True
b>a
True
b<a
False
a<=b
True
a<=b
True
a>=b
False
b<=a
False
b>=a
True
a!=b
True
b!=a
True
>>> a=5
>>> b=5
>>> a==b
True
>>> #Logical
>>> a=8
>>> b=10
>>> a<b and b>a
True
>>> a<=b and b>=a
True
>>> a!=b and a==b
False
>>> a<b or b>a
True
>>> a<=b or b>=a
True
>>> not True
False
>>> not False
True
>>> #Identify
>>> a=5
>>> type(a) is int
True
>>> type(a) is not int
False
>>> type(a) is float
False
>>> type(a) is not float
True
>>> #Membership
>>> a=4,5,6,7,8,9,10
>>> 10 in a
True
>>> 20 in a
False
>>> 30 in a
False
>>> 40 not in a
True
