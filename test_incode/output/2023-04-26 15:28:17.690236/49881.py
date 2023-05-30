#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        print("Current numbers: ", numbers)
        
        choice = input("Enter a number or q to quit: ")
        
        if choice == 'q':
            break
        
        number = int(choice)
        
        if number in numbers:
            numbers.remove(number)
            print("Number ", number, " removed")
        else:
            print("Number ", number, " not in the list")
            
        print("Current numbers: ", numbers)
        
        print("Press any key to continue...")
        
        input()
        
