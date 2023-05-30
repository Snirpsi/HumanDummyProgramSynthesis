#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or multiplyes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <word|number>" % sys.argv[0])
        sys.exit()
    
    word = ""
    number = 0
    
    if len(sys.argv) == 2:
        word = sys.argv[1]
        
    if len(sys.argv) == 3:
        number = int(sys.argv[2])
        
    if word == "word":
        word = input("Enter a word: ")
        
    if number == 1:
        number = int(input("Enter a number: "))
        
    print(number * word)
    
