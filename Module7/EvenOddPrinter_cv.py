import threading


class NumberPrinter:
    def __init__(self, max_num, /, start_with=0):
        assert start_with < max_num

        self.__limit = max_num
        self.__index = start_with
        self.__cv_1 = threading.Condition()
        self.__predicate_stack = [lambda: self.__index % 2 == 0, lambda: not self.__index % 2 == 0]

    def __call__(self):
        self.__even_printer(self.__predicate_stack.pop())

    def __even_printer(self, predicate: callable):
        while True:
            with self.__cv_1:
                self.__cv_1.wait_for(predicate)
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
    t1 = threading.Thread(target=sync_printer)
    t2 = threading.Thread(target=sync_printer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
