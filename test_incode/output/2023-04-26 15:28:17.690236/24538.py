#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or opens a list of words. """    
    
    # Read command line arguments
    words_list = sys.argv[1:]
    
    # Remove all words from the list
    words_list = filter(lambda x: x not in words_list, words_list)
    
    # Open the list for writing
    words_list = map(lambda x: open(x, 'w'), words_list)
    
    # Write the list to stdout
    words_list = map(lambda x: sys.stdout.write(x+'\n'), words_list)
    
    # Close the list
    words_list = map(lambda x: x.close(), words_list)
    
    # Close the program
    words_list = map(lambda x: sys.exit(), words_list)
    
    # Print the list
    words_list = map(lambda x: print(x, file=sys.stderr, end=' '), words_list)
    
    # Print the list
    words_list = map(lambda x: print(x, file=sys.stdout, end=' '), words_list)
    
    # Close the program
    words_list = map(lambda x: sys.exit(), words_list)
    
    # Print the list
    words_list = map(lambda x: print(x, file=sys.stdout, end=' '), words_list)
    
    # Close the program
    words_list = map(lambda x: sys.exit(), words_list)
    
    # Print the list
    words_list = map(lambda x: print(x, file=sys.stdout, end=' '), words_list)
    
    # Close the program
    words_list = map(lambda x: sys.exit(), words_list)
    
    # Print the list
    words_list = map(lambda x: print(x, file=sys.stdout, end=' '), words_list)
    
    # Close the program
    words_list = map(lambda x: sys.exit(), words_list)
    
    # Print the list
    words_list = map(lambda x: print(x, file=sys.stdout, end=' '), words_list)
    
    # Close the program
    words_list = map(lambda x: sys.exit(), words_list)
    
    # Print the list
    words_list = map(lambda x: print(x, file=sys.stdout, end=' '), words_list)
    
    # Close the program
    words_list = map(lambda x: sys.exit(), words_list)
    
    # Print the list
    words_list = map(lambda x: print(x, file=sys.stdout, end=' '), words_list)
    
    # Close the program
    words_list = map(lambda x: sys.exit(), words_list)
    
    # Print the list
    words_list = map(lambda x: print(x, file=sys.stdout, end=' '), words_list)
    
    # Close the program
    words_list = map(lambda x: sys.exit(), words_list)
    
    # Print the list
    words_list = map(lambda x: print(x, file=sys.stdout, end=' '), words_list)
    
    # Close the program
