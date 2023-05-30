#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that converts a list of numbers.
    #The program will exit when the user enters a number greater than 9
    #The program will then print out the list with the numbers 
    #in reverse order.
    while True:
        number = int(input('Enter a number: '))
        if number > 9:
            break
        else:
            numbers.append(number)
    print(numbers)
    
    
    
    
    
    

