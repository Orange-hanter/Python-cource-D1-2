from collections import Counter
import sys


def get_text_from_file() -> str | None:
    # todo implement configuration of the number of displayed elements through arguments
    if not len(sys.argv) == 2:
        raise RuntimeError("Path argument are not specified")
    path = sys.argv[1]
    with open(path, 'r') as file:
        return file.read()


def print_symbols_statistic(text: str, count: int = 10) -> None:
    print("Most common symbols are:")
    meta_inf = Counter(text)
    for smb, count in meta_inf.most_common(count):
        print(f"{repr(smb)} => {count} times")


if __name__ == '__main__':
    text = get_text_from_file()
    print_symbols_statistic(text)
