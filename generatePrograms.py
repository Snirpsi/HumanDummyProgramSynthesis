import os
import programEvaluator 
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from asyncio import subprocess
from treelib import Tree, Node



def dateStr():

    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()
    
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y_%m_%d_%H_%m_%s") 
    return dt_string  


class ProgramGenerator:
    #class to extend a given program using a transformer model 
    def __init__(self) -> None:
        #tokenizer = GPT2Tokenizer.from_pretrained("microsoft/codebert-base")
        #model = GPT2LMHeadModel.from_pretrained("microsoft/codebert-base")
        #SIC98/GPT2-python-code-generatorrite(s)
        #select the model 
        self.tokenizer = GPT2Tokenizer.from_pretrained("SIC98/GPT2-python-code-generator")
        self.model = GPT2LMHeadModel.from_pretrained("SIC98/GPT2-python-code-generator")
        self.prompts = []

    #appends new lines to the Program 
    def programAppender (self, inputProgramStr):
        input_ids = self.tokenizer.encode(inputProgramStr, add_special_tokens=False, return_tensors='pt')
        outputs = self.model.generate(input_ids=input_ids, max_length=64 + len(inputProgramStr),
        temperature=1.0,
        top_k=50,
        top_p=0.95,
        repetition_penalty=2.0,
        do_sample=True,
        num_return_sequences=50,
        length_penalty=2.0,
        early_stopping=True)
        #bitte mal testen was an outputs[1...n] steht
        decoded =[] 
        print("outputs:", outputs)
        for i,p in enumerate(outputs):
            decstr = ""
            decstr = ( self.tokenizer.decode(outputs[0], skip_special_tokens=True))
            decstr = decstr.replace("<EOS><BOS>","\n")
            decstr = decstr.replace("<BOS>","\n")
            decstr = decstr.replace("<EOS>","\n")
            decoded.append(decstr)
        return decoded

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
    generator  =  ProgramGenerator()
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
