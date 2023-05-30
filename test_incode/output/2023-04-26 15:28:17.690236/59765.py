#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words or prints numbers. """    
    
    words = ["cat", "dog", "mouse"]
    
    while True:
        for word in words:
            print(word)
        
        choice = input("Enter a number to continue: ")
        
        if choice == "exit":
            break
        else:
            words.remove(choice)
            
