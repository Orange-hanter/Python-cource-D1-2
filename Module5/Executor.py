import os
import sys


def print_stat():
    pid = os.getpid()
    print(f"pid:{pid}")
    os.system("/bin/ls -l /proc/%s/fd" %pid)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise RuntimeError("Path argument are not specified")
    cmd, args = sys.argv[1], sys.argv[2:]
    
    cp_env = os.environ.copy()
    parent_conn, child_conn = os.pipe()
    
    child_proc_id = os.fork()
    if child_proc_id:    #Parent process
        os.close(child_conn)
        with os.fdopen(parent_conn, 'r') as inp:
            print(inp.read())
    else:
        os.close(parent_conn)
        os.dup2(child_conn, 0)
        os.dup2(child_conn, 1)
        with os.fdopen(child_conn, 'w') as out:
            os.execve(cmd, args, cp_env)
