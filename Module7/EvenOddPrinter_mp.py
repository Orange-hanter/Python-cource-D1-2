from multiprocessing import Process, Lock


def print_num(start: int, l1: Lock, l2: Lock):
    for i in range(start, 1_000_001, 2):
        l1.acquire()
        print(i)
        l2.release()


if __name__ == '__main__':
    lock_1 = Lock()
    lock_2 = Lock()
    lock_2.acquire()
    process1 = Process(target=print_num, args=(0, lock_1, lock_2))
    process2 = Process(target=print_num, args=(1, lock_2, lock_1))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
