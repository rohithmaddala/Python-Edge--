Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Upper():
a='python'
a.upper()
'PYTHON'
#Lower():
b='CODE'
b.lower()
'code'
#Capitalize():
'python course'
'python course'
c='python course'
c.capitalize()
'Python course'
d='i am in class'
d.capitalize()
'I am in class'
#Title():
c.title()
'Python Course'
d.title()
'I Am In Class'
#checking conditions
a='data science'
a.islower()
True
a.isupper()
False
a.startwith('d')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.startwith('d')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith('d')
True
a.endswith('e')
True
b='datascience'
b.isalpha()
True
b.isdigit()
False
b.isalnum()
True
c='1234'
c.isdigit()
True
c.isalpha()
False
d='rohith8886'
d.isalnum()
True
d.isdigit()
False
d.isalpha()
False
#strip()
#lstrip(),rstrip()
a='   rohith     '
a.lstrip()
'rohith     '
a.rstrip()
'   rohith'
a.strip()
'rohith'
#split
a='python java c c++'
a.split()
['python', 'java', 'c', 'c++']
b='i am learning python'
b.split()
['i', 'am', 'learning', 'python']
#join()
a='apple','banana','mango'
''.join(a)
'applebananamango'
' '.join(a)
'apple banana mango'
'k'.join(a)
'applekbananakmango'
b='watermelon'
'l'.join(b)
'wlaltlelrlmlellloln'
#concatenation
a='python'
b='course'
print(a+b)
pythoncourse
print(a+' '+b)
python course
print(a+''+b)
pythoncourse
fname='rohith'
lname='maddala'
print(fname+lname)
rohithmaddala
print(fname+' '+lname)
rohith maddala
>>> print(fname.title()+' '+lname.title())
Rohith Maddala
>>> print(fname+' '+lname).title()
rohith maddala
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(fname+' '+lname).title()
AttributeError: 'NoneType' object has no attribute 'title'
>>> print((fname+' '+lname).title())
Rohith Maddala
>>> #formatting
>>> a=4
>>> b=7
>>> print(a+b)
11
>>> print('the sum is',a+b)
the sum is 11
>>> print('the sum is,a+b')
the sum is,a+b
>>> city='nlr'
>>> print('city is',city)
city is nlr
>>> #format method
>>> a='motu'
>>> b='patlu'
>>> print('hello {}{}'.format(a,b))
hello motupatlu
>>> 
... print('hello {} {}'.format(a,b))
hello motu patlu
>>> print('hello {} hello {}'.format(a,b))
hello motu hello patlu
>>> #fstring
>>> a='MS'
>>> b='Dhoni'
>>> print(f'hello {a}{b}')
hello MSDhoni
>>> print(f'hello {a} {b}')
hello MS Dhoni
>>> print(f'hello {a} hello {b}')
hello MS hello Dhoni
