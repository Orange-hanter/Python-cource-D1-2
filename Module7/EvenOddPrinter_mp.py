from multiprocessing import Process, Lock, Value


def print_num(index: Value, l1: Lock, l2: Lock):
    while index.value < 1_000_000:
        l1.acquire()
        print(index.value)
        index.value += 1
        l2.release()


if __name__ == '__main__':
    local_index = Value('i', 0)
    lock_1 = Lock()
    lock_2 = Lock()
    lock_2.acquire()
    process1 = Process(target=print_num, args=(local_index, lock_1, lock_2))
    process2 = Process(target=print_num, args=(local_index, lock_2, lock_1))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
