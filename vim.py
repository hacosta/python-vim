import subprocess
import tempfile
import os
import atexit

temp_filename = tempfile.mkstemp('.py')[1]
atexit.register(os.remove, temp_filename)

def vim(editor=''):
	""" Vim function, takes an alternative editor as a param. Will launch an editor instance and exec the code written to that file"""
	editor = editor or os.getenv('EDITOR') or 'vi'
	before = open(temp_filename).read()
	subprocess.call([editor, temp_filename])
	after = open(temp_filename).read()
	if before != after:
		new_locals = {}
		exec(after, globals(), new_locals)
		for k, v in new_locals.items():
			try: #nasty hack to include the vars back on the interpreter
				__builtin__[k] = v 
			except:
				__builtins__[k] = v

