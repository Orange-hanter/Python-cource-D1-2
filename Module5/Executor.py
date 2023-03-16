import os
import sys
from contextlib import redirect_stderr, redirect_stdout

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise RuntimeError("Path argument are not specified")
    cmd, args = sys.argv[1], sys.argv[2:]
    
    cp_env = os.environ.copy()
    parent_conn, child_conn = os.pipe()
    
    child_proc_id = os.fork()
    if child_proc_id:    #Parent process
        with os.fdopen(parent_conn, 'r') as inp:
            print("PARENT:")
            print(inp.read())
    else:
        with os.fdopen(child_conn, 'w') as out:
            with redirect_stdout(out):
                print("CHILD:")
                os.execve(cmd, args, cp_env)
