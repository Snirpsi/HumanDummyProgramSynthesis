#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or multiplyes a list of numbers. """    
    while True:
        words = []
        numbers = []
        
        while True:
            number = int(input("Enter a number: "))
            
            if number < 0:
                print("You entered a negative number!")
                continue
            
            if number > len(numbers):
                print("You entered a number that is bigger than the list!")
                continue
            
            numbers.append(number)
            
            if number == len(numbers):
                break
            
            words.append(str(number))
            
        print("The numbers are:")
        print(numbers)
        print("The words are:")
        print(words)
        
        answer = input("Do you want to continue? Y/N: ")
        
        if answer.lower() == "y":
            break
        else:
            print("Goodbye!")
            
    print("Goodbye!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    