import threading


class NumberPrinter:
    def __init__(self, max_num, /, start_with=0):
        assert start_with < max_num

        self._limit = max_num
        self._index = start_with

        self._event_1 = threading.Event()
        self._event_2 = threading.Event()
        self._event_2.set()

    def print_even(self):
        while True:
            self._event_1.wait()
            print(self._index, 'e')
            self._index += 1
            self._event_1.clear()
            self._event_2.set()
            if self._index >= self._limit: break

    def print_odd(self):
        while True:
            self._event_2.wait()
            print(self._index, 'o')
            self._index += 1
            self._event_2.clear()
            self._event_1.set()
            if self._index >= self._limit: break


if __name__ == '__main__':
    sync_printer = NumberPrinter(1_000_000, start_with=0)
    t1 = threading.Thread(target=sync_printer.print_even)
    t2 = threading.Thread(target=sync_printer.print_odd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
