#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    
    numbers = range(1,100)
    
    while True:
        print("The numbers are:")
        for number in numbers:
            print(number)
        
        choice = input("Would you like to add another number? Y/N: ")
        
        if choice == 'Y' or choice == 'y':
            numbers.append(int(input("Enter a number: ")))
            
        elif choice == 'N' or choice == 'n':
            break
            
        else:
            print("Sorry, I didn't understand your input.")
            
    print("Thanks for playing!")
    
