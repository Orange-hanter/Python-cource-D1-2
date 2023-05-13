import threading


class NumberPrinter:
    def __init__(self, max_num, /, start_with=0):
        assert start_with < max_num

        self._limit = max_num
        self.index = start_with

        self._lock_even = threading.Lock()
        self._lock_odd = threading.Lock()
        (self._lock_odd if self._is_index_even() else self._lock_even).acquire()

    def print_num(self):
        x = (self._lock_even, self._lock_odd) if self._is_index_even() else (self._lock_odd, self._lock_even)
        while True:
            self._do_logic(*x)
            if self.index >= self._limit:
                break

    def _is_index_even(self):
        return self.index % 2 == 0

    def _do_logic(self, lock1: threading.Lock, lock2: threading.Lock):
        lock1.acquire()
        print(self.index, threading.get_ident())
        self.index += 1
        lock2.release()


if __name__ == '__main__':
    sync_printer = NumberPrinter(100, start_with=43)
    t1 = threading.Thread(target=sync_printer.print_num)
    t2 = threading.Thread(target=sync_printer.print_num)
    [threading.Thread.start(obj) for obj in [t1, t2]]
    [threading.Thread.join(obj) for obj in [t1, t2]]
