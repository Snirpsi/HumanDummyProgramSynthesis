from asyncio import subprocess
import os
import programTester 


from transformers import GPT2Tokenizer, GPT2LMHeadModel


def dateStr():

    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()
    
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y_%m_%d_%H_%m_%s") 
    return dt_string  


class ProgramGenerator:
    def __init__(self) -> None:
        #tokenizer = GPT2Tokenizer.from_pretrained("microsoft/codebert-base")
        #model = GPT2LMHeadModel.from_pretrained("microsoft/codebert-base")
        #SIC98/GPT2-python-code-generatorrite(s)
        self.tokenizer = GPT2Tokenizer.from_pretrained("SIC98/GPT2-python-code-generator")
        self.model = GPT2LMHeadModel.from_pretrained("SIC98/GPT2-python-code-generator")
        self.prompts = []

    #appends new lines to the Program 
    def programAppender (self, inputProgramStr):
        input_ids = self.tokenizer.encode(inputProgramStr, add_special_tokens=False, return_tensors='pt')
        outputs = self.model.generate(input_ids=input_ids, max_length=64 + len(inputProgramStr),
        temperature=1.0,
        top_k=50,top_p=0.95,
        repetition_penalty=2.0,
        do_sample=True,
        num_return_sequences=1,
        length_penalty=2.0,
        early_stopping=True)
        #bitte mal testen was an outputs[1...n] steht
        decoded = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        decoded = decoded.replace("<EOS><BOS>","\n")
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
    
    outFolder = "ergebnisse/exp" + dateStr 
    try: 
        os.mkdir(outFolder) 
    except OSError as error: 
        print(error)  

    #the transformer to generate programs     
    generator  =  ProgramGenerator()
    valid_program = prompts[0]

    depth = 0
    max_trye = 0
    while depth < 10 and max_trye < 100:


        invalid_program = generator.programAppender("".join(valid_program))
        ##entfernen der letzten zeile des Programms 
        invalid_program = invalid_program[0: invalid_program.rfind('\n')]

        #invalid_program = prompts[0] 
        """
import numpy as np
if __name__ == "__main__":
    print(1+1)
        """

        print ("INPUT PROGRAM #########################################################################")
        print (invalid_program)
        print ("INPUT PROGRAM END #########################################################################")

        ret_val = None
        import subprocess
        import os
        try:
            #ret_val = programTester.testProgram(invalid_program)
            with open('tmp.py', 'w') as f:
                f.write(invalid_program)
            #execstring = 
            os.system("chmod +x tmp.py")
            retClass = subprocess.Popen(["python3", "tmp.py"])
            retClass.wait(5)
            ret_val = retClass.returncode
            print("> %s"%(ret_val))
        except Exception as e:
            print("fail to execute program %s"%(e))

        if (ret_val == 0 and not ("\"\"\"" in invalid_program)): 
            depth += 1
            valid_program = invalid_program

        max_trye += 1
        print("retval",ret_val, "depth", depth,"max_trye", max_trye)

    i = 0

    f = open(outFolder + "/" + str(i) + ".py", "w")
    f.write("".join(valid_program))
    f.close()




