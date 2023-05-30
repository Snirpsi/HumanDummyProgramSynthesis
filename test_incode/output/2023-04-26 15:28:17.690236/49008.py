#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Calculate word count
    word_count = len(args.split())
    
    # Print the result
    print("There are %d words in the file." % word_count)
    
    # Close the file
    f.close()
    
    # Close the program
    sys.exit(0)
    
