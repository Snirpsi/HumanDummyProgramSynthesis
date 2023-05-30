#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        number = input("Enter a number: ")
        
        if number in numbers:
            numbers.remove(number)
        else:
            print("That number is not in the list")
            
        print("The list now contains:", numbers)
        
        print("Would you like to play again? Y/N")
        
        answer = input("(y/n): ")
        
        if answer.lower() == "y":
            break
            
    print("The list contains:", numbers)
    
    print("Goodbye!")
    
