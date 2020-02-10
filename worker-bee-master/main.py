import threading
import work_module as wm
from thread import Thread
from multiprocessing import Process





mythreads = []
mythreads.append(Thread(1, "process1", wm.func_that_does_work))
mythreads.append(Thread(2, "process2", wm.more_work))
mythreads.append(Thread(3, "process3", wm.more_work_work))
for t in mythreads:
    t.start()


if __name__ == '__main__':
	p = Process(target=t.start)
	p.start()
	p.join()

