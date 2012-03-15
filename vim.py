#!/usr/bin/env/python2
import subprocess
import tempfile
import os
import imp

temp_filename = tempfile.mkstemp('.py')[1]

def vim(editor='vim'):
	editor = os.getenv('EDITOR') or editor
	before = open(temp_filename).read()
	subprocess.call([editor, temp_filename])
	after = open(temp_filename).read()
	if before != after:
		new_locals = {}
		exec(after, globals(), new_locals)
		print(new_locals)
		for k, v in new_locals.items():
			try: #nasty hack to include the vars back on the interpreter
				__builtin__[k] = v 
			except:
				__builtins__[k] = v

