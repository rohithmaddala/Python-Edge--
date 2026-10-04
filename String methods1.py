Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a='python course'
a[-1:-8:-2]
'ero '
a[-2:-12:-3]
'sont'
a[-4:-13:-4]
'uny'
a[2:6:1]
'thon'
a[4:-8:-2]
''
a[-4:-8:-2]
'uc'
a[::1]
'python course'
a[::-1]
'esruoc nohtyp'
#String methods:
#len()
a="Rohith"
len(a)
6
b='python course'
len(b)
13
c=''
len()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
len(c)
0
d=' '
len(d)
1
e='1234'
len(e)
4
e=1234
len(e)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    len(e)
TypeError: object of type 'int' has no len()
#Count()
a='oh7g?ub f8cd frhbi5n890h,jmup.m,jiubonhii.u,jmj
SyntaxError: unterminated string literal (detected at line 1)
a='twinkle twinkle little star'
count(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count('twinkle')
2
>>> a.count('t')
5
>>> a.count('l')
4
>>> a.count(' ')
3
>>> a.count('s')
1
>>> #Find a string:
>>> a="python"
>>> a[3]
'h'
>>> a.find('h')
3
>>> b='hello'
>>> b.find('l')
2
>>> b[2:4]
'll'
>>> #Escape sequences:
>>> #\n->ArithmeticError
>>> #\n->new line
>>> #\t->tab space
>>> a='name\nmobile no.:\tcity\nmail id:'
>>> print(a)
name
mobile no.:	city
mail id:
>>> a="name:Rohith\nmobile no.:8374839548\tcity:nellore\nmail id:rohithmaddala369@gmail.com"
>>> print(a)
name:Rohith
mobile no.:8374839548	city:nellore
mail id:rohithmaddala369@gmail.com
>>> #Replace:
>>> a="wait until you succeed"
>>> a.replace("wait","work")
'work until you succeed'
>>> b='python ML'
>>> b.replace('ML','AI')
'python AI'
