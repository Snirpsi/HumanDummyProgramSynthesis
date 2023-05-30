#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or removes a list of numbers. """    
    
    numbers = []
    
    while True:
        number = input("Enter a number: ")
        
        if number in numbers:
            print("Number already in list")
        else:
            numbers.append(number)
            
            if number == "q":
                print("Goodbye!")
                break
            
            print("Number added")
            
    print("Done")
    
