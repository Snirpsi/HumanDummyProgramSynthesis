#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words or multiplyes user input. """    
    words = []
    while True:
        word = input("Enter a word: ")
        words.append(word)
        if len(words) == 3:
            break
        else:
            print("Invalid input")
    
    multiplier = 1
    while True:
        multiplier = input("Enter a multiplier: ")
        multiplier = int(multiplier)
        if multiplier < 0:
            print("Invalid input")
        elif multiplier == 0:
            break
        else:
            words[0] *= multiplier
    
    for word in words:
        print(word)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
