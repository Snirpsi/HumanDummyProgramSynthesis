#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or opens numbers. """    
    
    # Open the file that contains the numbers.
    with open('numbers.txt', 'r') as numbers:
        numbers = numbers.readlines()
    
    # Get the user input from the user.
    while True:
        number = input('Enter a number: ')
        try:
            number = int(number)
        except ValueError:
            print('That is not a number!')
            continue
        
        # Check if the number was valid.
        if number < 0 or number > len(numbers):
            print('That number is out of range!')
            continue
        
        # Print the number.
        print('The number you entered is', number)
        
        # Continue the program if the user wants to continue the program.
        if input('Continue (y/n)? ').lower() != 'y':
            break
            
    # Close the file.
    numbers.close()
    
    # Close the program.
    print('Goodbye!')
    
# End of file.
