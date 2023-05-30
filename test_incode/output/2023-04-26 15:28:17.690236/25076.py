#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words or opens user input. """    
    while True:
        
        # Read user input
        words = input().split()
        
        # Multiply each word with its index
        words = [words[i] * i for i in range(len(words))]
        
        # Print the result
        print(' '.join(words))
        
        # 