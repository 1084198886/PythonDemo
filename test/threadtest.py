"""
线程
"""
import threading
import time
from queue import PriorityQueue


class MyThread(threading.Thread):
    globalPara = 0
    lock = threading.Lock()
    """
    通过直接从 threading.Thread 继承创建一个新的子类
    """

    def __init__(self, threadid, name, delay):
        threading.Thread.__init__(self)
        self.threadid = threadid
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程：" + self.name)
        self.lock.acquire()
        print_time(self, self.name, self.delay, 1)
        self.lock.release()
        print("退出线程：" + self.name)


def print_time(self, threadname, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadname, time.ctime(time.time())))
        counter -= 1
        MyThread.globalPara += 1  # 只能使用类名.属性名方式修改才能升序，否则是创建新变量
        print("globalPara修改成功:", self.globalPara)
        if counter <= 0:
            break


threads = []
t1 = MyThread(1, "Thread1", 1)
t2 = MyThread(2, "Thread2", 2)
t1.start()
t2.start()
threads.append(t1)
threads.append(t2)
for thread in threads:
    thread.join()
print("退出主线程")