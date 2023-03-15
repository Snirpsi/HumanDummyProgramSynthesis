import os
import programEvaluator 

#codebert python 

from asyncio import subprocess
from treelib import Tree, Node

from multiprocessing import Process, Queue, Lock
from queue import LifoQueue
from multiprocessing.managers import BaseManager

import time 
import random
import pdb #debugger
import traceback

import program_cleaner 
#os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
#os.environ["CUDA_VISIBLE_DEVICES"]="0"
from generator_transformer_model import ProgramGenerator

#set_start_method("spawn", force=True)


def dateStr():

    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()
    
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y_%m_%d_%H_%m_%s") 
    return dt_string  


generator  =  ProgramGenerator()
#Producer aka Program expander
def program_expander (queue_source:Queue, queue_destination:Queue):
    #take one otem from source 
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

    program_to_be_extendet = None

    #the transformer to generate programs
       
    
    while True:
        #take a node from the data and extract the program data from the node 
        program_dict =  queue_source.get()
        program_to_be_extendet = program_dict ["program"]
        program_to_be_extendet_ID = program_dict ["index"]
        #exeption can occurre when the iput vector is to long
        #kürze input bis es nichtmehr failt
        extended_programs = "\n" # naja
        try:
            extended_programs = generator.programAppender(program_to_be_extendet)
            
        except Exception as e: 
            print(e)
            traceback.print_exc()
            print("=============")
            fail=True #für dens ersten durchlauf
            program_head_list = [] #das was abgespalten wird
            program_tail =""
            #versuche solange eine programmerweiterung bis es klappt
            while(fail):
                fail = False
                print("transformer crash:", program_to_be_extendet_ID , "shortening program")
                #input to long remove first
                #line your_string.split('\n')[2:]
                #aufspalten in liste aus zeilen
                splited=extended_programs.split("\n",1)
                extended_programs=splited[1]
                #entfernen des ersten listenelements
                program_head_list.append(splited[0])
                #rest für generator
                program_to_be_extendet = splited[1]
                #
                try:
                    program_tail = generator.programAppender(program_to_be_extendet)
                except:
                    pass
            extended_programs = "\n".join(program_head_list)
            extended_programs += program_tail


        for i,p in enumerate(extended_programs):
            ##entfernen der letzten zeile des Programms da diese meist unvollständig sind
            #p = p[0: p.rfind('\n')]
            #entfernen von unnötigen leerzeichen
            p = program_cleaner.clean_code(p)
            #p="""print("HALLOOOOO")"""
            
            prog = {
                "index" : str(program_to_be_extendet_ID) + "." + str(i),
                "program" : p
            }
            #fügt valides Programm am ende der queue an 
            queue_destination.put(prog)
            #fügt valides programm am anfang der zeile an 
            #queue_destination.insert(0,prog)
            
def remove_lines_below_error(program_string, error_line):
    """
    Removes all lines below the given error line number in the specified Python program string.
    """
    lines = program_string.splitlines()
    lines = lines[:error_line-1]
    return '\n'.join(lines)


def program_evaluator(queue_source:Queue, queue_destination:Queue):

    evaluator = programEvaluator.ProgramEvaluator()

    #output folder
    dateStrS = dateStr()
    
    outFolder = "outputPrograms/exp" + dateStrS 
    try: 
        os.mkdir(outFolder) 
    except OSError as error: 
        print(error)  

    program_tree = Tree()

    #zur überprüfung von duplikaten der programme
    program_hash_set = set()

    i:int = 0
    while True:
        program_dict = queue_source.get()        
        program_to_be_evaluated = program_dict["program"]
        program_to_be_evaluated_ID = program_dict["index"]
        evaluation = evaluator.evaluateProgram(program_to_be_evaluated)
        #print("evaluating:", program_to_be_evaluated_ID, "executable?:" , evaluation.executable )
        print("Evaluation:\n"+ str(program_to_be_evaluated_ID)+ ":\n" +str(evaluation))
        print("Code:\n"+ "========START=========\n"+str(program_to_be_evaluated)+"\n"+"========END=========\n")
        if(evaluation.error_line != -1): # sind syntaxfehler vorhanden ?
            #entferne die entsprechenden codezeilen darunter
            program_to_be_evaluated = remove_lines_below_error(program_to_be_evaluated,evaluation.error_line)
            # second chance
            
            evaluation = evaluator.evaluateProgram(program_to_be_evaluated)
            print("Second Evaluation:\n"+ str(program_to_be_evaluated_ID)+ ":\n" +str(evaluation))
            pass

        if (evaluation.executable and hash(program_to_be_evaluated) not in program_hash_set ):
            # füge programm in queue ein 
            print("Insert: "+ str(program_to_be_evaluated_ID) )
            queue_destination.put(program_dict)
            #verhindere programme die schon exestieren füge hash set hinzu
            program_hash_set.add(hash(program_to_be_evaluated))
 
            program_version=  program_to_be_evaluated_ID
            f = open(outFolder + "/" + str(program_version) + ".py", "w")
            f.write(program_to_be_evaluated)
            f.close()

        i+=1 



# create manager that knows how to create and manage LifoQueues
class QueueManager(BaseManager):
    pass
QueueManager.register('LifoQueue', LifoQueue)



if __name__ == "__main__":

    print ("Instanciate QUEUE manager")
    manager = QueueManager()
    manager.start()


    print ("instanciating two Queues")
    #für Breitensuche Queue()
    #für Tiefensuche manager.LifoQueue() 
    queue_program_expansion = Queue() #manager.LifoQueue()#Queue()
    queue_program_evaluation = Queue() #manager.LifoQueue()#Queue()

    #setup  transformer
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

    prompts = []
    #lese inputtemplates ein
    import os
    inFolder = "/inputPrograms"
    for filename in os.listdir(os.getcwd() + inFolder):
        with open(os.path.join(os.getcwd() + inFolder, filename), 'r') as f:
            prompts.append(f.read())

    for i,p in enumerate (prompts):
        program = {
            "index": str(i),
            "program" : str(p)
        }
        queue_program_expansion.put(program)

    process_expansion = Process(target=program_expander, args=(queue_program_expansion,queue_program_evaluation))
    process_evaluation = Process(target=program_evaluator, args=(queue_program_evaluation,queue_program_expansion))

    process_expansion.start()
    process_evaluation.start()

    process_expansion.join()
    process_evaluation.join()



#OLD CODE
"""
if __name__ == "__main__":

    print("Hi")

    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

    prompts = []
    #lese inputtemplates ein
    import os
    inFolder = "/inputPrograms"
    for filename in os.listdir(os.getcwd() + inFolder):
        with open(os.path.join(os.getcwd() + inFolder, filename), 'r') as f:
            prompts.append(f.read())

    dateStr = dateStr()
    
    outFolder = "outputPrograms/exp" + dateStr 
    try: 
        os.mkdir(outFolder) 
    except OSError as error: 
        print(error)  

    #the transformer to generate programs     
    #generator  =  ProgramGenerator()
    valid_program = prompts[0]

    depth = 0
    max_trye = 0
    program_version = 0
    
    possibleProgramList = generator.programAppender("".join(valid_program))


    program_tree = Tree()
    program_tree.create_node("0",data=[valid_program,programEvaluator.ProgramEvaluator()])




    for programs in possibleProgramList:


        while depth < 10 and max_trye < 100:


            invalid_program = ""
            ##entfernen der letzten zeile des Programms da diese meist unvollständig sind
            invalid_program = invalid_program[0: invalid_program.rfind('\n')]

            #invalid_program = prompts[0] 
            print ("INPUT PROGRAM #########################################################################")
            print (invalid_program)
            print ("INPUT PROGRAM END #########################################################################")
            evaluator = programEvaluator.ProgramEvaluator()

            stats = evaluator.evaluateProgram(invalid_program)

            if ( stats.executable == True and not ("\"\"\"" in invalid_program)): 
                depth += 1
                valid_program = invalid_program
                f = open(outFolder + "/" + str(program_version) + ".py", "w")
                f.write("".join(valid_program))
                f.close()

            max_trye += 1
            print("retval", stats.executable, "depth", depth,"max_trye", max_trye)

    print ("FIN.")      

# %%
"""