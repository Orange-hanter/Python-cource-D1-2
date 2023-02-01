from collections import Counter
from io import TextIOWrapper
import sys


def read_data_chunk(file_object: TextIOWrapper, chunk_size: int = 33) -> str:
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        else:
            yield data
    file_object.close()


def get_binary_file():
    # todo implement configuration of the number of displayed elements through arguments
    if not len(sys.argv) == 2:
        raise RuntimeError("Path argument are not specified")
    path = sys.argv[1]
    file = open(path, 'rb')
    return read_data_chunk(file)


def symbols_statistic(byte_string_generator) -> Counter:
    meta_inf = Counter()
    buf = b""
    read_error = False

    for chunk in byte_string_generator:
        try:
            if read_error:
                decoded_text = (buf + chunk).decode("utf-8", errors="ignore")
            else:
                decoded_text = chunk.decode("utf-8")
        except UnicodeDecodeError as E:
            buf += chunk
            read_error = True
            continue

        if read_error:
            buf = b""
            read_error = False
        meta_inf.update(decoded_text)
    return meta_inf


def print_tables(table: Counter, top_count: int = 10):
    print("Most common symbols are:")
    for smb, count in table.most_common(top_count):
        print(f"{repr(smb)} => {count} times")


if __name__ == '__main__':
    byte_string_gen = get_binary_file()
    result = symbols_statistic(byte_string_gen)
    print_tables(result)
