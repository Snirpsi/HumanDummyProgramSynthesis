#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and adds user input. """    
    
    while True:
        word = input("Enter a word: ")
        
        if word == 'quit':
            break
        
        if word == 'exit':
            break
        
        word = word.lower()
        
        if word not in words:
            print(word + " is not in 