import threading


class NumberPrinter:
    def __init__(self, max_num, /, start_with=0):
        assert start_with < max_num

        self.__limit = max_num
        self.__start_value = start_with

    def __call__(self, l1: threading.Lock, l2: threading.Lock):
        begin = self.__start_value
        self.__start_value += 1
        for i in range(begin, self.__limit, 2):
            l1.acquire()
            print(i)
            l2.release()


if __name__ == '__main__':
    sync_printer = NumberPrinter(1_0, start_with=0)
    lock_1 = threading.Lock()
    lock_2 = threading.Lock()
    lock_2.acquire()
    t1 = threading.Thread(target=sync_printer, args=(lock_1, lock_2))
    t2 = threading.Thread(target=sync_printer, args=(lock_2, lock_1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
