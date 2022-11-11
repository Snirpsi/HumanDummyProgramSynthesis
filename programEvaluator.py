from time import sleep
import programStats
import os
import subprocess


class ProgramEvaluator:
    # this class evaluates a given program
    def __init__(self):
        pass

    
    def evaluateProgram(self,s) -> programStats.ProgramStats:
        stats = programStats.ProgramStats()
        stats.returnValue = self._program_exec(s)
        print("------------------> " ,stats.returnValue )
        if (stats.returnValue == 0):
            stats.executable = True
        else:
            stats.executable = False
        return stats

    def _program_exec(self,s):
        #eventuell hier art der exeption unterscheiden...
        try:
            #ret_val = programTester.testProgram(invalid_program)
            with open('tmp.py', 'w') as f:
                f.write(s)
            #execstring = 
            os.system("chmod +x tmp.py")
            retClass = subprocess.Popen(["python3", "tmp.py"])
            retClass.wait(5)
            print(retClass)
            ret_val = retClass.returncode
            print(ret_val)
            if(ret_val == None):
                return (0)
            return(ret_val)
        except Exception as e:
            print(e)
            return(-999)

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