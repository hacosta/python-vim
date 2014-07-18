import subprocess
import tempfile
import os
import os.path
import atexit

temp_filename = tempfile.mkstemp('.py')[1]
atexit.register(os.remove, temp_filename)


def vim(editor=''):
    """ Vim function, takes an alternative editor as a param. Will launch an editor instance and exec the code written to that file"""

    last_mtime = os.path.getmtime(temp_filename)
    editor = editor or os.getenv('EDITOR') or 'vi'
    subprocess.call([editor, temp_filename])

    if os.path.getmtime(temp_filename) != last_mtime:
        # File has been saved, update env
        last_mtime = os.path.getmtime(temp_filename)
        new_locals = {}
        try:
            exec(open(temp_filename).read(), globals(), new_locals)
        except SystemExit:
            pass
        for k, v in new_locals.items():
            try:  # hack to include the vars back on the interpreter
                __builtin__[k] = v
            except:
                __builtins__[k] = v
