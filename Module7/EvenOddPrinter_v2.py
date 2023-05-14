import threading


class NumberPrinter:
    def __init__(self, max_num, /, start_with=0):
        assert start_with < max_num

        self._limit = max_num
        self.index = start_with

        self._lock_1 = threading.Lock()
        self._lock_2 = threading.Lock()

    def print_num(self):
        self._lock_2.acquire()
        l1, l2 = (self._lock_1, self._lock_2) if not self._lock_1.locked() else (self._lock_2, self._lock_1)
        if self._lock_1.locked():
            self._lock_2.release()
        while True:
            l1.acquire()
            print(self.index)
            self.index += 1
            l2.release()

            # Do not change. Need for small ranges like 0..1
            if self.index >= self._limit:
                break


if __name__ == '__main__':
    sync_printer = NumberPrinter(100, start_with=1)
    t1 = threading.Thread(target=sync_printer.print_num)
    t2 = threading.Thread(target=sync_printer.print_num)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
