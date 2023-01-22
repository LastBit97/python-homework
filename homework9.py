import threading
import time


def counter(interval, name_thread):
    print(name_thread, "start")
    for i in range(10, 0, -1):
        print(name_thread, i)
        time.sleep(interval)
    print(name_thread, "stop")


t1 = threading.Thread(target=counter, args=(1, 'first thread:'), daemon=True)
t2 = threading.Thread(target=counter, args=(1, 'second thread:'), daemon=True)
t1.start()
t2.start()
t1.join()
t2.join()
