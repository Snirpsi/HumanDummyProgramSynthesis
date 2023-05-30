#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers or multiplyes a list of words. """    
    
    import sys
    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: python add.py word1 word2 word3 ...")
        exit(1)
    
    for word in words:
        
        if word == "+":
            print(str(int(sys.argv[1])+int(sys.argv[2])))
            
        elif word == "*":
            print(str(int(sys.argv[1])*int(sys.argv[2])))
            
        else:
            print("Usage: python add.py + *")
            exit(1)
            
