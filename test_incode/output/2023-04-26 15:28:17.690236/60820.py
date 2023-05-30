#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers and converts user input. """    
    
    # Create a list to hold the user's input
    numbers = []
    
    # Get the user's input from the user
    while True:
        number = int(input("Enter a number: "))
        numbers.append(number)
        
        # Check if the user wants to quit
        if number == -1:
            break
        
    # Print the user's input
    print("The numbers you entered are:")
    print(numbers)
    
    # Convert the user's input to a string
    string = str(numbers)
    
    # Print the converted string
    print("The converted string is:")
    print(string)
    
    # Print the converted string to a file
    with open('converted_string.txt', 'w') as converted_file:
        converted_file.write(string)
        
    # Print the converted string to a file
    with open('converted_string.txt', 'r') as converted_file:
        converted_string = converted_file.read()
        
    # Print the converted string to a file
    with open('converted_string.txt', 'w') as converted_file:
        converted_file.write(converted_string)
        
    # Print the converted string to a file
    with open('converted_string.txt', 'r') as converted_file:
        converted_string = converted_file.read()
        
    # Print the converted string to a file
    with open('converted_string.txt', 'w') as converted_file:
        converted_file.write(converted_string)
        
    # Print the converted string to a file
    with open('converted_string.txt', 'r') as converted_file:
        converted_string = converted_file.read()
        
    # Print the converted string to a file
    with open('converted_string.txt', 'w') as converted_file:
        converted_file.write(converted_string)
        
    # Print the converted string to a file
    with open('converted_string.txt', 'r') as converted_file:
        converted_string = converted_file.read()
        
    # Print the converted string to a file
    with open('converted_string.txt', 'w') as converted_file:
        converted_file.write(converted_string)
        
    # Print the converted string to a file
    with open('converted_string.txt', 'r') as converted_file:
        converted_string = converted_file.read()
        
    # Print the converted string to a file
    with open('converted_string.txt', 'w') as converted_file:
        converted_file.write(converted_string)
        
    # Print the converted string to a file
    with open('converted_string.txt', 'r') as converted_file:
        converted_string = converted_file.read()
        
    # Print the converted string to a file
    with open('converted_string.txt', 'w') as converted_file:
        converted_file.write(converted_string)
        
    # Print the converted string to a file
    with open('converted_string.txt', 'r') as converted_file:
        converted_string = converted_file.read()
        
    # Print the converted string to a file
    with open('converted_string.txt', 'w') as converted_file:
        converted_file.write(converted_string)
        
    # Print 