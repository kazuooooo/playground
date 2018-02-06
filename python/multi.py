#conding: utf-8
from multiprocessing import Pool, Process
import time
import os

# def print_time():
#     tm = time.localtime(time.time())
#     return time.strftime("%M:%S", tm)
#
#
# def print_time():
#     tm = time.localtime(time.time())
#     return time.strftime("%M:%S", tm)
#
#
# def sum_print(a, b, c):
#     time.sleep(1)
#     print
#     "pid: %d, sum: %d, time: %s " % (os.getpid(), a + b + c, print_time())
#     # return "pid: %d, sum: %d, time: %s " % (os.getpid(), a+b+c, print_time())
#
#
# def sum(a, b, c):
#     time.sleep(1)
#     return "pid: %d, sum: %d, time: %s " % (os.getpid(), a + b + c, print_time())
#
#
# def print_square(x):
#     time.sleep(1)
#     print
#     "pid: %d, square: %d, time: %s" % (os.getpid(), x * x, print_time())
#
#
# def square(x):
#     time.sleep(1)
#     return "pid: %d, square: %d, time: %s" % (os.getpid(), x * x, print_time())
#
#
# if __name__ == '__main__':
#     print("CPU Core:" + str(multiprocessing.cpu_count()))
#     print("Process:")
#     sum_p = Process(target=sum_print, args(2,3,4))
#     sum_p.start()
#     square_p.start()
#     sum_p.join()
#     square_p.join()

# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))

def f(name):
    print('hello', name)


if __name__ == '__main__':
    # Processのオブジェクトを生成
    p = Process(target=f, args=('bob',))
    #
    p.start()
    p.join()