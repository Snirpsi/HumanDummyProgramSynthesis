#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words. """    
    words = []
    
    # Read words from stdin and add them to the list
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    # Print the list
    print(words)
    
    # Write the list to stdout
    sys.stdout.write('\n'.join(words))
    
    # Close the file
    sys.stdout.close()
    
    # Close the 