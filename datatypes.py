Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> a=987
>>> type(a)
<class 'int'>
>>> b=69
>>> type(b)
<class 'int'>
>>> c=2.0
>>> type(c)
<class 'float'>
>>> d=0.5
>>> type(d)
<class 'float'>
>>> e='rohith'
>>> type(e)
<class 'str'>
>>> f="python"
>>> type(f)
<class 'str'>
>>> g='''movies'''
>>> type(g)
<class 'str'>
>>> h=5=9j
SyntaxError: cannot assign to literal
>>> h=5+9j
>>> type(h)
<class 'complex'>
>>> i=7j
>>> type(i)
<class 'complex'>
>>> j=true
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    j=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> j=True
>>> type(j)
<class 'bool'>
>>> k=False
>>> type(k)
<class 'bool'>
