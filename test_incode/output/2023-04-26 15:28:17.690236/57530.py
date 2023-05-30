#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Remove all words from file
    with open(args[0], 'r') as file:
        lines = file.readlines()
        
    # Write new file
    with open(args[1], 'w') as file:
        for line in lines:
            line = line.strip()
            if line:
                file.write(line)
                file.write('\n')
    
    # Print success message
    print('Done')
