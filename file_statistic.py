from collections import Counter
import sys


def read_file() -> str | None:
    # todo implement configuration of the number of displayed elements through arguments
    if not len(sys.argv) == 2:
        return None
    with open(sys.argv[1], 'r') as file:
        return file.read()


def parse_text(text: str) -> Counter:
    return Counter(text)


def log(meta_inf: Counter, count: int = 10) -> None:
    print("Most common symbols are:")
    for item in meta_inf.most_common(count):
        omg = repr(item[0].encode())[2:-1]
        print(f"'{omg}' => {item[1]} times")


if __name__ == '__main__':
    text = read_file()
    if (not text):
        print("File not found!")
        exit()
    meta_inf = parse_text(text)
    log(meta_inf)
