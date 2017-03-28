Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> primt "hello again"
SyntaxError: invalid syntax
>>> print "hello again" + 1

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print "hello again" + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> 
================ RESTART: C:/Users/User/Desktop/PrintTest.py ================
I love pizza!
pizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizza
yumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyum
I'm full.
>>> 
================= RESTART: C:/Users/User/Desktop/NumGuess.py =================

Traceback (most recent call last):
  File "C:/Users/User/Desktop/NumGuess.py", line 1, in <module>
    import randon
ImportError: No module named randon
>>> 
================= RESTART: C:/Users/User/Desktop/NumGuess.py =================

Traceback (most recent call last):
  File "C:/Users/User/Desktop/NumGuess.py", line 2, in <module>
    secret = randon.randint(1, 99)
NameError: name 'randon' is not defined
>>> 
================= RESTART: C:/Users/User/Desktop/NumGuess.py =================
AHOY! I'm the Dread Pirate Roberts, and I have a secret!
It is a number from 1 to 99. I'll give you 6 tires.
What's yer guess? 
3

Traceback (most recent call last):
  File "C:/Users/User/Desktop/NumGuess.py", line 9, in <module>
    guess = input("What's yer guess? ")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
