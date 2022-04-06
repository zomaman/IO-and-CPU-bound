import time
import requests

from threading import Thread
from multiprocessing import Process


# Замеряет время выполнения
def measure_time(func):
    def measure():
        begin = time.time()
        n = func()
        print("Задание", n)
        print("Time:", time.time() - begin, end="\n\n")

    return measure


# Для IO bound
def t():
    res = requests.get('https://google.com')


# Для CPU bound
def countdown():
    i = 0
    while i < 5_000_000:
        i += 1


# Задание 1
@measure_time
def one():
    res = list()
    for i in range(10):
        res.append(requests.get('https://google.com'))
    return 1


# Задание 2
@measure_time
def two():
    threads = list()
    for i in range(10):
        threads.append(Thread(target=t))

    for thrd in threads:
        thrd.start()
    for thrd in threads:
        thrd.join()

    return 2


# Задание 3
@measure_time
def three():
    processes = list()
    for i in range(10):
        processes.append(Process(target=t))

    for prc in processes:
        prc.start()
    for prc in processes:
        prc.join()

    return 3


# Задание 4
@measure_time
def four():
    for i in range(10):
        countdown()
    return 4


# Задание 5
@measure_time
def five():
    threads = list()
    for i in range(10):
        threads.append(Thread(target=countdown))

    for thrd in threads:
        thrd.start()
    for thrd in threads:
        thrd.join()

    return 5


# Задание 6
@measure_time
def six():
    processes = list()
    for i in range(10):
        processes.append(Process(target=countdown))

    for prc in processes:
        prc.start()
    for prc in processes:
        prc.join()

    return 6


if __name__ == "__main__":
    # IO bound
    one()
    two()
    three()

    # CPU bound
    four()
    five()
    six()
