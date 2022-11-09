from multiprocessing.connection import wait
import re
from threading import Thread
from time import sleep
from os import system
import stopableThread
from stopableThread import ThreadWithExc

import subprocess


def threaded_func(arg):
    while True: 
        print("running Thread:" ) 
        sleep(1)


def _program_exec(s):
    with open('tmp.py', 'w') as f:
        f.write(s)
    
    
    #execstring = "echo \'\n" + str(s) + "\' | python3"
    
    execstring = "python3 tmp.py"
    print (execstring)
    return system(execstring)

#tests a program p in athread for 1 second 
#lieber subprocesses verwenden ? 
def testProgram(s) -> int:
    with open('tmp.py', 'w') as f:
        f.write(s)
    execstring = ["./tmp.py"]

    retClass = subprocess.Popen([execstring])
    retClass.wait()
    print ("returnclass" , retClass )
    code = retClass.returncode
    print("-------------> %s"%(code))
    return code
    
    rval =  print(_program_exec(s))
    
    return _program_exec(rval)
    exec_ret_val = 0
    thread = ThreadWithExc(target=_program_exec,args=(s,))
    print ("executing ...")
    thread.start()
    tid = thread.ident()
    thread.join(5)
    print("wakeup")
    if(thread.is_alive()):
        print("killing Program Timeout")
        stopableThread._async_raise(tid, exctype= type( Exception("threadstopper")))
    print(thread,tid)
    
    if(thread.is_alive()):
        print("killing Program Timeout")
        stopableThread._async_raise(tid, exctype= type( Exception("threadstopper")))
   
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