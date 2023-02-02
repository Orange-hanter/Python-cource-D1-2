from collections import Counter
import os
import psutil
import sys


def isMemoryEnough(file_size_in_bites: int):
    free_memory = psutil.virtual_memory().available
    file_size_in_MB = file_size_in_bites / (1024 * 1024)
    modifier = 0.8
    return (free_memory * modifier) > file_size_in_MB


def symbols_statistic(byte_string: str, meta_inf: Counter) -> Counter:
    decoded_text = (byte_string).decode("utf-8", errors="ignore")
    meta_inf.update(decoded_text)
    return meta_inf


def print_tables(table: Counter, top_count: int = 10) -> None:
    print("Most common symbols are:")
    for smb, count in table.most_common(top_count):
        print(f"{repr(smb)} => {count} times")


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        raise RuntimeError("Path argument are not specified")

    meta_inf = Counter()
    path = sys.argv[1]

    with open(path, 'rb') as file:
        if not isMemoryEnough(os.stat(path).st_size):
            while True:
                data = file.readline()
                if not data:
                    break
                symbols_statistic(data, meta_inf)
        else:
            symbols_statistic(file.read(), meta_inf)

    print_tables(meta_inf)
