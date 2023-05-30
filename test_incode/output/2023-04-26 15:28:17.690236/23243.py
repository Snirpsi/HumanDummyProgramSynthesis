#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers and prints a list of words. """    
    
    words = []
    
    # Read a file and store its content in a list
    lines = open('words.txt').readlines()
    
    # Iterate over the lines of the file
    for line in lines:
        # Split the line into words
        words.append(line.split())
        
    # Print the list of words
    for word in words:
        print(word)
        
    # Print the length of the list
    print(len(words))
    
    # Print the length of the first word
    print(words[0][0])
    
    # Print the length of the last word
    print(words[-1][0])
    
    # Print the length of the first word with spaces
    print(words[0][0].ljust(10))
    
    # Print the length of the last word with spaces
    print(words[-1][0].ljust(10))
    
    # Print the length of the first word with spaces
    print(words[0][0].ljust(20) + words[0][1])
    
    # Print the length of the last word with spaces
    print(words[-1][0].ljust(20) + words[-1][1])
    
    # Print the length of the first word with spaces
    print(words[0][0].ljust(30) + words[0][1])
    
    # Print the length of the last word with spaces
    print(words[-1][0].ljust(30) + words[-1][1])
    
    # Print the length of the first word with spaces
    print(words[0][0].ljust(40) + words[0][1])
    
    # Print the length of the last word with spaces
    print(words[-1][0].ljust(40) + words[-1][1])
    
    # Print the length of the first word with spaces
    print(words[0][0].ljust(50) + words[0][1])
    
    # Print the length of the last word with spaces
    print(words[-1][0].ljust(50) + words[-1][1])
    
    # Print the length of the first word with spaces
    print(words[0][0].ljust(60) + words[0][1])
    
    # Print the length of the last word with spaces
    print(words[-1][0].ljust(60) + words[-1][1])
    
    # Print the length of the first word with spaces
    print(words[0][0].ljust(70) + words[0][1])
    
    # Print the length of the last word with spaces
    print(words[-1][0].ljust(70) + words[-1][1])
    
    # Print the length of the first word with spaces
    print(words[0][0].ljust(80) + words[0][1])
    
    # Print the length of the last word with spaces
    print(words[-1][0].ljust(80) + words[-1][1])
    
    # Print the length of the first word with spaces
    print(words[0][0].ljust(90) + words[0][1])
    
    # Print the length of the last word with spaces
    print(words[-1][0].ljust(90) + words[-1]