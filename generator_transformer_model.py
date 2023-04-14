# os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"]="1"
# import gc
# import sys
# import time
# from numba import jit, cuda
# import torch
# from torch.multiprocessing import Pool, Process, set_start_method

class ProgramGenerator:
    def __init__(self) -> None:

        self.was_initialized = False
        # set_start_method("spawn", force=True)

    # wird erst von dem tread initialisiert von dem es tazächlich zur generierung gebraucht wird.

    def __inofficial_init__(self) -> None:
        import torch
        from transformers import GPT2Tokenizer, GPT2LMHeadModel, AutoTokenizer, AutoModelForCausalLM

        if torch.cuda.is_available():
            dev = "cuda:1"
        else:
            dev = "cpu"
        self.device = torch.device(dev)

        print("Usind device:", str(self.device))

        self.tokenizer = GPT2Tokenizer.from_pretrained(
            "SIC98/GPT2-python-code-generator")
        self.model = GPT2LMHeadModel.from_pretrained(
            "SIC98/GPT2-python-code-generator")
        self.model.to(self.device)
        self.prompts = []
        self.was_initialized = True

    # appends new lines to the Program
    def programAppender(self, inputProgramStr):
        if (not self.was_initialized):
            print("Fist Time Initialisation")
            self.__inofficial_init__()
        input_ids = self.tokenizer.encode(
            inputProgramStr, add_special_tokens=False, return_tensors='pt').to(self.device)

        self.outputs = self.model.generate(
            input_ids=input_ids,
            max_new_tokens=265,
            min_length=64,
            max_length=64 + len(inputProgramStr),  # keine maximahle länge
            temperature=0.5,
            top_k=100,
            top_p=0.90,
            repetition_penalty=20.0,
            do_sample=True,
            num_return_sequences=200,  # anzahl der sequenzen die zurückkommen
            length_penalty=1000,
            early_stopping=False
        )
        # outputs[1...n] sind die verschiedenen vektoren
        decoded = []
        # print("outputs:", outputs)
        for i, p in enumerate(self.outputs):
            decstr = ""
            decstr = (self.tokenizer.decode(
                self.outputs[i], skip_special_tokens=True))
            decstr = decstr.replace("<EOS><BOS>", "\n")
            decstr = decstr.replace("<BOS>", "\n")
            decstr = decstr.replace("<EOS>", "\n")
            decstr = decstr.replace("< EOS > < BOS >", "\n")
            decstr = decstr.replace("< BOS >", "\n")
            decstr = decstr.replace("< EOS >", "\n")
            decoded.append(decstr)
            # print("Error:" + str(input_ids), file=sys.stderr)
            # input_ids.detach()
            # ädel input_ids
            # gc.collect()
            # time.sleep(10)
        return decoded


if __name__ == "__main__":
    generator = ProgramGenerator()
    extended_programs = ["n=3\n"]
    while True:
        extended_programs = generator.programAppender([extended_programs[0]])
        print("\n=======================================\n")
        print(extended_programs)
