import threading


class NumberPrinter:
    def __init__(self, max_num, /, start_with=0):
        assert start_with < max_num

        self._limit = max_num
        self._start_num = start_with

        self._event_even = threading.Event()
        self._event_odd = threading.Event()

        self._isEven = int(self._start_num % 2)
        if self._isEven:
            self._event_even.set()
            self._event_odd.clear()
        else:
            self._event_even.clear()
            self._event_odd.set()

    def print_even(self):
        modifier = 1 if not self._isEven else 0
        for i in range(self._start_num + modifier, self._limit, 2):
            self._event_even.wait()
            print(i, "even")
            self._event_even.clear()
            self._event_odd.set()

    def print_odd(self):
        modifier = 1 if self._isEven else 0
        for i in range(self._start_num + modifier, self._limit, 2):
            self._event_odd.wait()
            print(i, "odd")
            self._event_odd.clear()
            self._event_even.set()


if __name__ == '__main__':
    sync_printer = NumberPrinter(100, start_with=2)
    t1 = threading.Thread(target=sync_printer.print_even)
    t2 = threading.Thread(target=sync_printer.print_odd)
    [threading.Thread.start(obj) for obj in [t1, t2]]
    [threading.Thread.join(obj) for obj in [t1, t2]]
