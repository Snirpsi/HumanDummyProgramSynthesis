from threading import Thread
from time import sleep
from os import system
import stopableThread
from stopableThread import ThreadWithExc


def threaded_func(arg):
    while True: 
        print("running Thread:" ) 
        sleep(1)


def _program_exec(s):
    execstring = "echo \'\n" + str(s) + "\' | python3"
    print (execstring)
    return system(execstring)

#tests a program p in athread for 1 second 
def testProgram(s):
    thread = ThreadWithExc(target=_program_exec,args=(s,))
    print ("executing ...")
    thread.start()
    tid = thread.ident()
    print(thread,tid)
    sleep(5)
    print("wakeup")
    if(thread.is_alive()):
        print("killing Program Timeout")
        stopableThread._async_raise(tid, exctype= type( Exception("threadstopper")))
    thread.join()
    print("Fin")


if __name__ == "__main__":
    ret_val =_program_exec("""print("Test")""")
    print(ret_val)

    """
    thread = ThreadWithExc(target=threaded_func,args=(10,))
    thread.start()
    tid = thread.ident
    print(thread)
    
    sleep(5)
    print("wakeup")
    stopableThread.py._async_raise(tid, exctype= type( Exception("threadstopper")))
    thread.join()
    print("Fin")
    """