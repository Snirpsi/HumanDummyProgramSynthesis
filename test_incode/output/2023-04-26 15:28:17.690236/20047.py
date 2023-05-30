#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words or removes numbers. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Calculate list of words
    words = []
    for arg in args:
        words.append(arg.lower())
    
    # Remove numbers
    words = [word for word in words if word.isdigit()]
    
    # Print results
    print("\n".join(words))
    
