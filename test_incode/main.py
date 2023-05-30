from typing import List

import torch
import tokenizers
from transformers import AutoModelForCausalLM, AutoTokenizer
import json

if torch.cuda.is_available():
    dev = "cuda:1"
else:
    dev = "cpu"
device = torch.device(dev)
print("initialize tokenizer")
#tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot")
tokenizer = AutoTokenizer.from_pretrained("facebook/incoder-1B")
print("initialize model")
#model = AutoModelWithLMHead.from_pretrained("codeparrot/codeparrot")
model = AutoModelForCausalLM.from_pretrained("facebook/incoder-1B")
print("move model to device " + dev )
model.to(device)


while True:
    print ("Gebe ein programm ein:\n")
    inputProgramStr = input()
    print("toknisiere input")
    input_ids = tokenizer.encode(
            inputProgramStr, add_special_tokens=False, return_tensors='pt').to(device)
    print("generiere output")
    outputs = model.generate(
            input_ids=input_ids,
            max_new_tokens=265,
            min_length=0,
            #max_length=64 + len(inputProgramStr),  # keine maximahle länge
            temperature=0.2,
            top_k=100,
            #top_p=0.90,
            repetition_penalty=20.0,
            do_sample=True, # disables greede seach 
            num_return_sequences=10,#200  # anzahl der sequenzen die zurückkommen
            #length_penalty=1000,
            #early_stopping=False
            extra_sentinel: bool=True,
            max_retries: int=1
        )
    print("decodiere output")
    for i, p in enumerate(outputs):
        print("{solution: 3d}: ==============================================".format(solution=i))
        decstr = (tokenizer.decode(p, skip_special_tokens=True,clean_up_tokenization_spaces=False))
        print(decstr)
