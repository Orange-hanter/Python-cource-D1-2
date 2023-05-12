import threading


class NumberPrinter:
    def __init__(self, max_num, /, start_with=0):
        assert start_with < max_num

        self._limit = max_num
        self.index = start_with

        self._lock = threading.Lock()
        self._lock_your_turn = threading.Lock()
        self._assertion = False

    def print_num(self, text="", /, only_odd=True):
        while not self._assertion:
            with self._lock:
                if only_odd != self._is_index_even():  # true in case the "even" thread try process even index
                    # print(f"Have you heard of our god saver Emperor? {threading.get_ident()}")
                    self._lock_your_turn.acquire()
                if self._lock_your_turn.locked():
                    print(self.index, text)
                    self.index += 1
                    self._lock_your_turn.release()

            if self.index >= self._limit:
                break

    def _is_index_even(self):
        return self.index % 2 == 0


if __name__ == '__main__':
    sync_printer = NumberPrinter(100, start_with=43)
    t1 = threading.Thread(target=sync_printer.print_num, args=("odd",), kwargs={"only_odd": True})
    t2 = threading.Thread(target=sync_printer.print_num, args=("even",), kwargs={"only_odd": False})
    [threading.Thread.start(obj) for obj in [t1, t2]]
    [threading.Thread.join(obj) for obj in [t1, t2]]
