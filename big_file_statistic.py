from collections import Counter
from io import TextIOWrapper
import sys


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
        for chunk in file.readlines():
            symbols_statistic(chunk, meta_inf=meta_inf)

    print_tables(meta_inf)
