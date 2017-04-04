Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import easygui

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import easygui
ImportError: No module named easygui
>>> import easygui

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import easygui
ImportError: No module named easygui
>>> import easygui
>>> easygui.msgbox('This is a basic message box.', ' Title Goes Here')
'OK'
>>> import easygui
>>> user_response=easygui.msgbox('This is a basic message box.', 'Title Goes Here')
>>> print user_response
OK
>>> import easygui
>>> easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
'Chocolate'
>>> import easygui
>>> user_response=easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
>>> user_response=easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry', 'blueberry', 'melon'))
>>> import easygui
>>> flavor=easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
>>> easygui.msgbox('You picked'+flavor)
'OK'
>>> import easygui
>>> flavor = easygui.choicebox('Whatis is your favorite flavor.', choices = ['Chocolate', 'Vanilla', 'Strawberry'])
[0]
>>> easygui.msgbox('You picked ' + flavor)
'OK'
>>> import random, easygui
>>> seret = random.randit(1,99)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    seret = random.randit(1,99)
AttributeError: 'module' object has no attribute 'randit'
>>> import random, easygui
>>> secret = random.randit(1,99)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    secret = random.randit(1,99)
AttributeError: 'module' object has no attribute 'randit'
>>> secret=random.randint(1,99)
>>> guess=0
>>> tries=0
>>> easygui.msgbox("I have a secret! It is a number from 1 to 99. I'll give you 6 tries")
'OK'
>>> while guess != secret and tries < 6:
	guess = easygui.integerbox("Please guess the number ~ (" + str(tries+1) + ")")
	if not guess: break
	if guess < secret:
		easygui.msgbox(str(guess) + " is too low, try again!")
	elif guess > secret:
		easygui.msgbox(str(guess) + " is too high, try more!")
	 tries = tries + 1
 if guess == secret:
    easygui.msgbox("Wow! You got it! Found my secret, well done!^^")
 else:
    easygui.msgbox("Sorry but No more chances.... The number was " + str(secret))

  File "<pyshell#34>", line 9
    tries = tries + 1
                    ^
IndentationError: unindent does not match any outer indentation level
>>> import random, easygui
secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox("I have a secret! It is a number from 1 to 99.   I'll give you 6 tries")
while guess != secret and tries < 6:
    guess = easygui.integerbox("Please guess the number ~  (" + str(tries+1) + ")")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low, try again!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high, try more!")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("Wow! You got it! Found my secret, well done!^^")
else:
    easygui.msgbox("Sorry but No more chances.... The number was " + str(secret))

>>> 
>>> import random, easygui
>>> secret = random.randint(1,99)
>>> guess=0
>>> tries=0
>>> easygui.msgbox("I have a secret! It is a number from 1 to 99.   I'll give you 6 tries")
'OK'
>>> while guess != secret and tries < 6:
	guess = easygui.integerbox("Please guess the number ~ (" + str(tries+1) + ")")
	if not guess: break
	if guess < secret:
		easygui.msgbox(str(guess) + " is too low, try again!")
	elif guess > secret :
		easygui.msgbox(str(guess) + " is too high, try more!")
	tries = tries + 1
        if guess == secret :
		easygui.msgbox("Wow! You got it! Found my secret, well done!^^")
	else:
		easygui.msgbox("Sorry but No more chances... The number was " +str(secret))

		
'OK'
'OK'
'OK'
>>> 
