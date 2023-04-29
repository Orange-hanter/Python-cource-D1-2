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
        os.chdir(self.prev_dir)

    def __repr__(self):
        return f'Pushd({self.new_dir})'


def scenario(do_exception=False):
    print(os.getcwd())
    try:
        with Pushd('/'):
            print(os.getcwd())
            if do_exception: raise RuntimeError
    except Exception:
        print("Exception handled")
    print(os.getcwd())


if __name__ == '__main__':
    print("Scenario with exception:")
    scenario(True)
    print("\nScenario without exception:")
    scenario(False)
