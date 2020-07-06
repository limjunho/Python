import time
import threading
from threading import Thread

def thread_function():
    i = 0
    while(True):
        print("thread_function("+str(i)+")")
        i += 1
        time.sleep(3)

if __name__ == "__main__":
    thread = threading.Thread(target=thread_function, args=())
    thread.start()

    i = 0
    while(True):
        print("main thread("+str(i)+")")
        i += 1
        time.sleep(1) 
