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
        parent_conn = os.fdopen(parent_conn, 'r')
        while True:
            data = parent_conn.readline()
            if not data:
                break
            print("P:", data, end="")
        parent_conn.close()

    else:
        os.close(parent_conn)
        os.dup2(child_conn, 1)
        os.dup2(child_conn, 2)
        sys.stdout = open(os.devnull, 'w')
        os.execve(cmd, args, cp_env)
