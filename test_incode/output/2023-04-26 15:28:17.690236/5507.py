#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or calculates a list of words. """    
    
    words = []
    
    while True:
        
        command = input("Enter a command: ")
        
        if command == "quit":
            break
        
        elif command == "add":
            
            words.append(input("Enter a word: "))
            
        elif command == "list":
            
            print(" ".join(words))
            
        else:
            print("Invalid command")
            
    
