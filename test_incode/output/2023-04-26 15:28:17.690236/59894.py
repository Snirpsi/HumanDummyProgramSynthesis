#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Remove all words from file
    with open(args[0], 'r') as file:
        lines = file.readlines()
        
        # Remove all words from file
        with open(args[1], 'w') as file:
            for line in lines:
                words = line.split()
                
                # Remove all words from file
                for word in words:
                    file.write(word)
                file.write('\n')
                
    # Print the result
    print('Removed all words from file "{}".'.format(args[1]))
