python-vim
==========

Want to quickly test the output of a function, so you open up your trusty python REPL and start typing away.

After a while you need nested for loops, or want to save a copy of the stuff you wrote. Or copy just a bit of code from your project.

Here's where python-vim comes in, it allows you to run a vim() session inside your REPL env, after you save your code, it will get executed, don't worry! you'll still have access to everything you defined inside your vim session.

Usage
-----

$ python

\>\>\> from vim import vim

\>\>\> vim()

 # Vim session opens, type your code here, save and exit
```python
foo = 'bar'
for i in foo:
    print i
```
\<esc\>:x

b

a

r

\>\>\> foo

'bar'

Protip:
-------
Add this to your .pythonrc file:

from vim import *


Installing
----------
* Using pip:
```
$ pip install python-vim
```
