#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words or removes numbers. """    
    while True:
        word = ""
        number = ""
        
        word = input("Enter a word: ")
        number = input("Enter a number: ")
        
        if word == "" or number == "":
            print("Goodbye!")
            break
        
        if number.isdigit():
            number = int(number)
            
        if word == number:
            print("Goodbye!")
            break
        
        print("Sorry, that's not right.")
        
    print("Goodbye!")
    
