Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Positive String Slicing:
a='codegnan it solutions'
b='vijayawada is a royal city'
a[4:8]
'gnan'
a[9:11]
'it'
a[12:]
'solutions'
b[16:21]
'royal'
b[22:]
'city'
b[:11]
'vijayawada '
#Negative String Slicing:
a='codegnan IT solutions'
b='vijayawafda is a royal city'
a[-17:-13]                                                                                           17:
...     
SyntaxError: invalid syntax
>>> a[-17:-13]
'gnan'
>>> a[-12:-10]
'IT'
>>> a[-9:0]
''
>>> a[-9:]
'solutions'
>>> b[-10:-5]
'royal'
>>> b[-4:]
'city'
>>> b[-26:-16]
'ijayawafda'
>>> b[-27:-16]
'vijayawafda'
>>> #Striding:
>>> a='Machine learning'
>>> a[::2]
'Mcielann'
>>> a[::4]
'Miln'
>>> a[5:9]
'ne l'
>>> a[:11]
'Machine lea'
>>> a[::8]
'Ml'
>>> b='cloud computing'
>>> b[2:12:4]
'ocu'
>>> b[1:8:2]
'lu o'
>>> b[1:14:5]
'lct'
>>> b[1:13:3]
'ldou'
>>> b[3:9:4]
'uo'
