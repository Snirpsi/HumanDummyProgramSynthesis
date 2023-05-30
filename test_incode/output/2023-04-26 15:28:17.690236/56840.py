#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words and multiplyes a port. """    
    
    words = []
    
    # Read file into list
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Multiply each word in the list by its corresponding port
    words = [word * port for word, port in zip(words, ports)]
    
    # Print the result
    print(words)
    
