#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words or calculates a port. """    
    
    words = []
    
    while True:
        words.append(input("Enter a word: "))
        
        if len(words) == 3:
            print(calculate_port(words[0], words[1], words[2]))
            
        elif len(words) == 2:
            print(calculate_port(words[0], words[1]))
            
        else:
            print("Too many words. Try again.")
            
