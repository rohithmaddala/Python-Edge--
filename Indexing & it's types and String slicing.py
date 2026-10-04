Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Indexing
a='nellore'
a[0]
'n'
a[1]
'e'
a[2]
'l'
a[3]
'l'
a[4]
'o'
a[5]
'r'
a[6]
'e'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
'nellore'
b="I am in Class
SyntaxError: unterminated string literal (detected at line 1)
b="I am in class"
b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]+b[8]+b[9]+b[10]+b[11]+b[12]
'I am in class'
b[0]
'I'
b[2]+b[3]
'am'
b[5]+b[6]
'in'
b[8]+b[9]+b[10]+b[11]+b[12]
'class'
b[1]
' '
b[4]
' '
b[7]
' '
b[13]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b[13]
IndexError: string index out of range
>>> c="I am learning Python Fullstack"
>>> c[14]+c[15]+c[16]c[17]+c[18]+c[19]=c[20]
SyntaxError: invalid syntax
>>> c[14]+c[15]+c[16]+c[17]+c[18]+c[19]+c[20]
'Python '
>>> c[21]+c[22]+c[23]+c[24]
'Full'
>>> c[5]+c[6]+c[7]+c[8]+c[9]
'learn'
>>> c[2]+c[3]
'am'
>>> d="Time is precious"
>>> d[-8]+d[-7]+d[-6]+d[-5]+d[-4]+d[-3]+d[-2]+d[-1]
'precious'
>>> d[-16]+d[-15]+d[-14]+d[-13]
'Time'
>>> e="vijayawada is a royal city"
>>> e[-4]+e[-3]+e[-2]+e[-1]
'city'
>>> e[-10]+e[-9]+e[-8]
'roy'
>>> e[-10]+e[-9]+e[-8]+e[-7]+e[-6]
'royal'
>>> e[-24]+e[-23]+e[-22]+e[-21]+e[-20]+e[-19]+e[-18]+e[-17]+e[-16]+e[-15]+e[-14]
'jayawada is'
>>> #String Slicing
>>> a='codegnan'
>>> a[0]+a[1]+a[2]+a[3]
'code'
>>> a[0:4]
'code'
>>> a[:4]
'code'
>>> a[4:8]
'gnan'
>>> a[4;]
SyntaxError: invalid syntax
>>> a[4:]
'gnan'
