# This is a sample Python script.
import random

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
pronomes = ["A",]
subjects = ["programm","function","minimal webserver", "endless loop"]
binders = ["that",]
verbs = ["stores","calculates","returns","enumerates","iterates over","adds","removes","converts","prints","opens","multiplyes"]
objects = ["numbers", "words", "fruits", "a list of words", "a list of numbers","a port","all ports", "user input" ]
conjunctions = ["and", "or"]


def generate():
    ergstr = ""

    ergstr = " ".join([random.choice(pronomes), random.choice(subjects),random.choice(binders),random.choice(verbs),random.choice(objects)])
    r=random.randint(0, 1)
    if r == 0:
        ergstr = " ".join([ergstr, random.choice(conjunctions), random.choice(verbs), random.choice(objects)])
    ergstr += "."
    return ergstr
    
    
if __name__ == '__main__':
    for i in range(0,10):
        print (generate())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
