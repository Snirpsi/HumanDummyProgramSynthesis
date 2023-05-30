#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and opens a list of numbers. """    
    
    words = []
    
    # Open the file words.txt
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    
    # Open the file numbers.txt and read it line by line
    with open('numbers.txt', 'r') as numbers:
        for line in numbers:
            numbers.append(line.strip())
    
    # Print the words and numbers in order
    print('Words:')
    for word in words:
        print(word)
    print('Numbers:')
    for number in numbers:
        print(number)
    
