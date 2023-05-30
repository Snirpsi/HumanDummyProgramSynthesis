#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and enumerates words. """    
    
    # Open the file that contains the numbers and words to enumerate
    with open('words.txt', 'r') as file:
        numbers = file.read().splitlines()
    
    # Enumerate the words and print them out
    for number in numbers:
        print(number)
    
    # Close the file
    file.close()
    
    # Close the program
    exit()
    
# End of program
