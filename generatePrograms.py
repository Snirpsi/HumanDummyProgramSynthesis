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

if __name__ == "__main__":

    print("Hi")

    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

    #tokenizer = GPT2Tokenizer.from_pretrained("microsoft/codebert-base")
    #model = GPT2LMHeadModel.from_pretrained("microsoft/codebert-base")
    #SIC98/GPT2-python-code-generator
    tokenizer = GPT2Tokenizer.from_pretrained("SIC98/GPT2-python-code-generator")
    model = GPT2LMHeadModel.from_pretrained("SIC98/GPT2-python-code-generator")
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

    possibleResultProgram = []

    possibleResultProgram.append(prompts[0])

    depth = 0

    while depth < 10:
        #input_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors='pt')
        input_ids = tokenizer.encode("".join(possibleResultProgram), add_special_tokens=False, return_tensors='pt')
        outputs = model.generate(input_ids=input_ids,
                                max_length=64 + len("".join(possibleResultProgram)),
                                temperature=0.5,
                                top_k=50,
                                top_p=0.95,
                                repetition_penalty=1.0,
                                do_sample=True,
                                num_return_sequences=1,
                                length_penalty=2.0,
                                early_stopping=True)
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print("#" * 20)
        print("".join(possibleResultProgram))
        print("v" * 20)
        print(decoded)
        print("=" * 20)
        print ("EXECUTING!!!!!!!!!!!!!!!!!!!!!!")

        possibleResultProgram.append(decoded.replace("<EOS><BOS>","\n"))

        assambledProg = "".join(possibleResultProgram)
        ret_val = 1
        try:
            ret_val = programTester.testProgram(assambledProg)
        except:
            print("fail to execute program")

        if (ret_val != 0): 
            del possibleResultProgram [-1] #entferne das zuletzt hinzugefügte element 
        else:
            depth += 1

        print("retval",ret_val, "depth", depth)

    i = 0

    f = open(outFolder + "/" + str(i) + ".py", "w")
    f.write("".join(possibleResultProgram))
    f.close()




