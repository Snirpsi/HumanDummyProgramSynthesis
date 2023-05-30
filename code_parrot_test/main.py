import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
from transformers import pipeline

if torch.cuda.is_available():
    dev = "cuda:1"
else:
    dev = "cpu"
device = torch.device(dev)
print("initialize tokenizer")
tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot")
print("initialize model")
model = AutoModelWithLMHead.from_pretrained("codeparrot/codeparrot")
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
            temperature=0.5,
            top_k=100,
            #top_p=0.90,
            #repetition_penalty=20.0,
            do_sample=True,
            num_return_sequences=10,#200  # anzahl der sequenzen die zurückkommen
            #length_penalty=1000,
            #early_stopping=False
        )
    print("decodiere output")
    for i, p in enumerate(outputs):
        print("{solution: 3d}: ==============================================".format(solution=i))
        decstr = (tokenizer.decode(p, skip_special_tokens=True))
        print(decstr)
