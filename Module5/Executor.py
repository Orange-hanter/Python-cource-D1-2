import os
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise RuntimeError("Path argument are not specified")
    cmd, args = sys.argv[1], sys.argv[2:]

    cp_env = os.environ.copy()
    parent_conn, child_conn = os.pipe()

    child_proc_id = os.fork()
    if child_proc_id:  # Parent process
        os.close(child_conn)
        with os.fdopen(parent_conn, 'r') as my_stdout:
            while True:
                data = my_stdout.readline()
                if not data: break
                print("P:", data, end="")

    else:
        os.close(parent_conn)
        os.dup2(child_conn, 1)
        os.dup2(child_conn, 2)
        with open(os.devnull, 'r') as nul:
            os.dup2(nul.fileno(), 0)
            os.execve(cmd, args, cp_env)
