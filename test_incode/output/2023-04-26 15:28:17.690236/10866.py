#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or calculates a list of numbers. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        
        if word == 'add':
            num = input("Enter a number: ")
            num = float(num)
            
            print(word + " " + str(num))
            
        elif word == 'list':
            num = input("Enter a number: ")
            num = float(num)
            
            print(str(num))
            
        else:
            print("Invalid command")
            
