import random
import json
from operator import itemgetter # to sort list of dicts

f = open('task_fragments.json')
program_task_fragments = json.load(f)
f.close()

program_fragment_order = ["start", "subject", "binder", "verb", "object"]

#program_fragment_ids = []

#for i in range(0, 100):
def generate():
    fragment_ids = []
    prompt = []
    code = []
    for fragment_type in program_fragment_order:
        rand = random.randint(0,len(program_task_fragments[fragment_type])-1)
        fragment_ids.append(rand)
        prompt.append(program_task_fragments[fragment_type][rand]["text"])
        if (program_task_fragments[fragment_type][rand]["code-fragments"]):
            code.extend(program_task_fragments[fragment_type][rand]["code-fragments"])
    prompt_text = " ".join(prompt) + "."
    print(code)
    #remove code duplicates 
    code = [dict(t) for t in {tuple(d.items()) for d in code}]
    code.sort(key=itemgetter("priority"))
    code_str_list = []
    for c in code:
        if c["code"]:
            code_str_list.append(c["code"])

    #print(prompt_text)
    #print(code_str_list)
    code_text = "\n".join(code_str_list) + "\n    #" + prompt_text
    return code_text
    # print(code_text)
    #print("="*100)


#for i,fragment in enumerate(program_task_fragments["start"]):
#    print(i,fragment)
if __name__ == "__main__":
    for i in range(0, 100):
        print ("="*100)
        print (generate())

