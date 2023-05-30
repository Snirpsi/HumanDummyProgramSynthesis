import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("facebook/incoder-6B", revision="float16", torch_dtype=torch.float16, low_cpu_mem_usage=True)
tokenizer = AutoTokenizer.from_pretrained("facebook/incoder-6B")

output = tokenizer.decode(tokenizer.encode("from ."), clean_up_tokenization_spaces=False)
print("output")