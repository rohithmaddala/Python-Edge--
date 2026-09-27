Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#bitwise operators
#&,|,~,^,<<,>>
a=3
b=5
a&b
1
bin(a)
'0b11'
bin(b)
'0b101'
a=2
b=4
bin(a)
'0b10'
bin(b)
'0b100'
a&b
0
0
0
0b=8
SyntaxError: invalid binary literal
a=6
b=8
bin(a)
'0b110'
bin(b)
'0b1000'
a&b
0
a=2
b=4
bin(2)
'0b10'
bin(4)
'0b100'
>>> bin(a)
'0b10'
>>> bin(b)
'0b100'
>>> a&b
0
>>> #|(or)
>>> a=3
>>> b=6
>>> a|b
7
>>> bin(a)
'0b11'
>>> bin(b)
'0b110'
>>> a=5
>>> b=7
>>> bin(a)
'0b101'
>>> bin(b)
'0b111'
>>> a|b
7
>>> a=8
>>> b=4
>>> a|b
12
>>> bin(a)
'0b1000'
>>> bin(b)
'0b100'
>>> #~
>>> a=3
>>> ~a
-4
>>> -(a+1)
-4
>>> b=-3
>>> ~b
2
