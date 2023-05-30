#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words or calculates fruits. """    
    
    # Read input from stdin
    words = sys.stdin.read().split()
    
    # Print the result
    for word in words:
        print(word)
        
    # Calculate fruit count
    fruits = sum(1 for word in words if word != '')
    
    # Print the result
    print('Number of fruits: {}'.format(fruits))
    
