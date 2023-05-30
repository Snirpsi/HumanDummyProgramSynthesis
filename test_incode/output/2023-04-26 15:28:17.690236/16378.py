#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    while True:
        words = []
        for x in range(int(input("How many words?"))):
            words.append(input("Enter a word: "))
        
        words = [x.lower() for x in words]
        
        for word in words:
            print(word*