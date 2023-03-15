from time import sleep
import programStats
import os
import subprocess
import py_compile


def extract_line_number_from_error(error_string):
        """
        Extracts the line number from an error message or traceback string that includes the substring ", line ".
        Returns the line number as an integer.
        """
        line_index = error_string.find(", line ")
        if line_index == -1:
            # ", line " substring not found in error message
            return None
        line_number_str = error_string[line_index + 7:].split()[0] # +7 for mofing behind ", line " string.
        try:
            line_number = int(line_number_str)
        except ValueError:
            # Unable to parse line number as integer
            return None
        return line_number

class ProgramEvaluator:
    # this class evaluates a given program
    def __init__(self):
        pass

    
    def evaluateProgram(self,s) -> programStats.ProgramStats:
        stats = programStats.ProgramStats()
        return_dict = self._compile(s)#self._program_exec(s)
        stats.returnValue = return_dict["ret_val"]
        stats.error_line = return_dict["error_line"]
        #print("------------------> " ,stats.returnValue )
        if (stats.returnValue == 0):
            stats.executable = True
        else:
            stats.executable = False
        return stats

    def _compile(self,s) -> programStats.ProgramStats:
        return_dict = {
            "ret_val" : 0,
            "error_line" : -1,
        }
        try:
            with open('tmp.py', 'w') as f:
                f.write(s)
                
            try:
                py_compile.compile("tmp.py")
            except (SyntaxError, IndentationError) as err:
                print("err:",err)
                print("err_dec:",err.decode('utf-8'))
                
                error_line = extract_line_number_from_error(err.decode('utf-8'))
                if (error_line):
                    return_dict["error_line"] = error_line

            pass
            
        except Exception as e:
            print(e)
            return_dict["ret_val"]=-999
            return(return_dict)
            
                
            
        
    def _program_exec(self,s):
        #eventuell hier art der exeption unterscheiden...
        return_dict = {
            "ret_val":-998,
            "error_line":-1
            }
        
        try:
            #ret_val = programTester.testProgram(invalid_program)
            with open('tmp.py', 'w') as f:
                f.write(s)
            #execstring = 
            os.system("chmod +x tmp.py")
            retClass = subprocess.Popen(["python3", "tmp.py"], stderr=subprocess.PIPE)
            out,err = retClass.communicate(input=None,timeout=5.0)
            #ret = subprocess.communicate(input=None, timeout=None)
            #print(ret.__str__())
            #retClass.wait(5)
            #
            #print(out,err.decode('utf-8'))
            error_line = extract_line_number_from_error(err.decode('utf-8'))
            
            if (error_line):
                return_dict["error_line"] = error_line
            #print(retClass)
            #error = retClass.__str__()
            #print (retClass.__str__())
            ret_val = retClass.returncode
            #print(ret_val)
            if(ret_val == None):
                return_dict["ret_val"] = 0
                return return_dict
            return_dict["ret_val"] = ret_val
            return(return_dict)
        except Exception as e:
            print(e)
            return_dict["ret_val"]=-999
            return(return_dict)



if __name__ == "__main__":
    e = ProgramEvaluator()

    #ret_val =e._program_exec("""print(hallo")""")
    #print(ret_val)
    print(e.evaluateProgram("""print(hallo")""").__str__())
    
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