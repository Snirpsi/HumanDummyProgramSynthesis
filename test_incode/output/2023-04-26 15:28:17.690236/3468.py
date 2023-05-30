#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        words = f.readlines()
        
    # Remove empty lines
    words = [word.strip() for word in words]
    
    # Remove duplicates
    words = list(set(words))
    
    # Print all words
    for word in words:
        print(word)
        
    # Write words to file
    with open('words.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')
            
