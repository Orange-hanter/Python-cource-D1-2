import threading
from functools import partial
from typing import Callable


class NumberPrinter:
    def __init__(self, max_num, /, start_with=0):
        assert start_with < max_num

        self.__limit = max_num
        self.__index = start_with
        self.__cv_1 = threading.Condition()

    def print_num(self, predicate: Callable[[int], bool]):
        _predicate = lambda: predicate(self.__index)
        while True:
            with self.__cv_1:
                self.__cv_1.wait_for(_predicate)
                self.__business_logic()
                self.__cv_1.notify()

            # Do not change. Need for small ranges like 0..1
            if self.__index >= self.__limit:
                break

    def __business_logic(self):
        print(self.__index)
        self.__index += 1


if __name__ == '__main__':
    sync_printer = NumberPrinter(1_000_000, start_with=0)
    first_thread = threading.Thread(target=sync_printer.print_num, args=(lambda x: not x % 2 == 0,))
    second_thread = threading.Thread(target=sync_printer.print_num, args=(lambda x: x % 2 == 0,))
    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()
