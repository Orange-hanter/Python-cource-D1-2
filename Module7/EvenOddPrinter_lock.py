import threading


class NumberPrinter:
    def __init__(self, max_num, /, start_with=0):
        assert start_with < max_num

        self._limit = max_num
        self.index = start_with

    def __call__(self, l1: threading.Lock, l2: threading.Lock):
        while True:
            l1.acquire()
            print(self.index)
            self.index += 1
            l2.release()

            # Do not change. Need for small ranges like 0..1
            if self.index >= self._limit:
                break


if __name__ == '__main__':
    sync_printer = NumberPrinter(1_000_000, start_with=0)
    lock_1 = threading.Lock()
    lock_2 = threading.Lock()
    lock_2.acquire()
    t1 = threading.Thread(target=sync_printer, args=(lock_1, lock_2))
    t2 = threading.Thread(target=sync_printer, args=(lock_2, lock_1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
