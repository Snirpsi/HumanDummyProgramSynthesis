#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    # Read input from stdin
    lines = sys.stdin.readlines()
    
    # Convert each line into a list of words
    words = [line.split()[0] for line in lines]
    
    # Print the word counts
    print('\n'.join(['%s: %d' % (word, len(word)) for word in words]))
    
    # 