#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words or multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python word.py <word>")
    else:
        word = sys.argv[1]
        
        if word == "word":
            print(" ".join(word))
        elif word == "multiply":
            multiplier = 1
            for number in sys.argv[2:]:
                multiplier = multiplier * int(number)
            print(multiplier)
        else:
            print("Error: invalid word")
    
