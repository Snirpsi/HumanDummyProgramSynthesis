#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or iterates over user input. """    
    
    words = []
    
    # Read user input from stdin
    while True:
        line = input('Enter a word: ')
        
        # Check if word is empty
        if not line:
            break
        
        # Append word to list
        words.append(line)
        
    # Print the list
    print('\n'.join(words))
    
    # 