#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or enumerates user input. """    
    
    # Get the user input
    words = []
    while True:
        words.append(input("Enter a word: "))
        if len(words) == 0: break
    
    # Multiply each word
    total = 0
    for word in words:
        total += int(word)
    
    # Print the result
    print("The total of {0} words is {1}".format(len(words), total))
    
    # Quit if user enters EOF
