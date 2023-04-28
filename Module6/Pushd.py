"""
Write class Pushd supporting context manager protocol, working as of pushd/popd from Bash
(see https://en.wikipedia.org/wiki/Pushd_and_popd)
"""
import os


class Pushd:
    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.prev_dir = None

    def __enter__(self):
        self.prev_dir = os.getcwd()
        os.chdir(self.new_dir)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            os.chdir(self.prev_dir)
        else:
            return False

    def __repr__(self):
        return f'Pushd({self.new_dir})'


if __name__ == '__main__':
    print(os.getcwd())
    with Pushd('/'):
        print(os.getcwd())
    print(os.getcwd())
