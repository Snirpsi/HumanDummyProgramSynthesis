import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AutoTokenizer, AutoModelForCausalLM
from numba import cuda

if torch.cuda.is_available():  
    dev = "cuda:0" 
else:  
    dev = "cpu"  
device = torch.device(dev)  

if torch.cuda.is_available():  
    dev2 = "cuda:1" 
else:  
    dev2 = "cpu" 
device2 = torch.device(dev2)

print(torch.cuda.is_available())
print(str(device))

tokenizer = GPT2Tokenizer.from_pretrained("SIC98/GPT2-python-code-generator")#.to(device)
model = GPT2LMHeadModel.from_pretrained("SIC98/GPT2-python-code-generator")
#tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
#model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B")

model.to(device)
print(torch.cuda.is_available())

inputProgramStr= "#the main method\n"
while True:
    input_ids = tokenizer.encode(inputProgramStr, add_special_tokens=False, return_tensors='pt').to(device)

    outputs = model.generate(
                input_ids=input_ids, 
                max_new_tokens=265,
                min_length=64,
                #max_length=64 + len(inputProgramStr), #keine maximahle länge
                temperature=0.5,
                top_k=100,
                top_p=0.90,
                repetition_penalty=20.0,
                do_sample=True,
                num_return_sequences=1000, # anzahl der sequenzen die zurückkommen 
                length_penalty=1000, 
                early_stopping=False
            )
            #outputs[1...n] sind die verschiedenen vektoren 
    decoded =[] 
        #print("outputs:", outputs)
    for i,p in enumerate(outputs):
        decstr = ""
        decstr = ( tokenizer.decode(outputs[i], skip_special_tokens=True))
        #decstr = decstr.replace("<EOS><>BOS","\n")
        #decstr = decstr.replace("<BOS>","\n")
        #decstr = decstr.replace("<EOS>","\n")
        decoded.append(decstr)
    #print(decoded)
    print("decoded:", decoded)

