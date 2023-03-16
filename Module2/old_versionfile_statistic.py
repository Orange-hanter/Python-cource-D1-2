from collections import Counter
import sys


def read_binary_file():
    # todo implement configuration of the number of displayed elements through arguments
    if not len(sys.argv) == 2:
        raise RuntimeError("Path argument are not specified")
    path = sys.argv[1]
    with open(path, 'rb') as file:
        return file.read()

    
def print_symbols_statistic(byte_string, count: int = 10) -> None:
    print("Most common symbols are:")
    meta_inf = Counter(byte_string.decode('utf-8', errors='ignore'))
    for smb, count in meta_inf.most_common(count):
        print(f"{repr(smb)} => {count} times")


if __name__ == '__main__':
    byte_string  = read_binary_file()
    print_symbols_statistic(byte_string )
