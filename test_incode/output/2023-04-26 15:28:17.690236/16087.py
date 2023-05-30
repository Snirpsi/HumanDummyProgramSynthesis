#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == "word":
            word = input("Enter a word: ")
            
            print(word)
        
        elif word == "list":
            words = input("Enter a word: ")
            
            for word in words.split():
                print(word)
        
        else:
            print("Invalid input")
        
    else:
        print("No word given")
        
