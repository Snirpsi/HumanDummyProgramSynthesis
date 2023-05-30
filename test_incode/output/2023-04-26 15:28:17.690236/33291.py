#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or calculates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = sys.argv[1]
        
        if number.isdigit():
            print(number)
        else:
            word = number.split()
            print(" ".join(word))
    else:
        print("Usage: python3 words.py")
