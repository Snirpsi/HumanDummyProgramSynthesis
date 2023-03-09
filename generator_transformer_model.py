import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AutoTokenizer, AutoModelForCausalLM

class ProgramGenerator:
    def __init__(self) -> None:
        if torch.cuda.is_available():  
            dev = "cuda:0" 
        else:  
            dev = "cpu"  
        self.device = torch.device(dev)  
        
        print("Usind device:",str(self.device))

        self.tokenizer = GPT2Tokenizer.from_pretrained("SIC98/GPT2-python-code-generator")
        self.model = GPT2LMHeadModel.from_pretrained("SIC98/GPT2-python-code-generator")
        self.model.to(self.device)
        
        self.prompts = []
        

    #appends new lines to the Program 
    def programAppender (self, inputProgramStr):
        input_ids = self.tokenizer.encode(inputProgramStr, add_special_tokens=False, return_tensors='pt').to(self.device)
        outputs = self.model.generate(
            input_ids=input_ids, 
            max_new_tokens=265,
            min_length=64,
            #max_length=64 + len(inputProgramStr), #keine maximahle länge
            temperature=0.75,
            top_k=100,
            top_p=0.90,
            repetition_penalty=20.0,
            do_sample=True,
            num_return_sequences=500, # anzahl der sequenzen die zurückkommen 
            length_penalty=1000, 
            early_stopping=False
        )
        #outputs[1...n] sind die verschiedenen vektoren 
        decoded =[] 
        #print("outputs:", outputs)
        for i,p in enumerate(outputs):
            decstr = ""
            decstr = ( self.tokenizer.decode(outputs[i], skip_special_tokens=True).to(self.device))
            #decstr = decstr.replace("<EOS><>BOS","\n")
            #decstr = decstr.replace("<BOS>","\n")
            #decstr = decstr.replace("<EOS>","\n")
            decoded.append(decstr)
        #print(decoded)
        return decoded