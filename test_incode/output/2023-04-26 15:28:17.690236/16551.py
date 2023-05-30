#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and multiplyes words. """    
    
    words = []
    
    # Read words from stdin and store them in list
    for line in sys.stdin:
        words.append(line.strip())
        
    # Calculate and store product of words in list
    product = 1
    for word in words:
        product *= int(word)
    
    # Print the product of words to stdout
    print(product)
    
