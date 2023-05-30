#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers and opens a list of words. """    
    numbers = input("Enter a list of numbers: ")
    words = open("words.txt", "w")
    words.write(numbers)
    words.close()
    print("The words are stored.")
    
