#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers. """    
    numbers = []
    
    # Open the file with the numbers and append them to the list
    with open("numbers.txt", "r") as file:
        for line in file:
            numbers.append(int(line))
    
    # Print the list to the screen
    print("The numbers in the file are:")
    print(numbers)
    
    # Close the file
    file.close()
    
    # Close the program
    exit(0)
    
# End of file

<|/ file filename=