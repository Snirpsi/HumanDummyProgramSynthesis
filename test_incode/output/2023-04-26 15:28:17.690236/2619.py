#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port and calculates a list of words. """    
    
    # Read in command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('port', help='The port to remove')
    args = parser.parse_args()
    
    # Remove port from list of words
    words = removePort(args.port)
    
    # Print list of words
    print(words)
    
    # Print number of words in list
    print(len(words))
    
    # Print first word in list
    print(words[0])
    
    # Print last word in list
    print(words[-1])
    
    # Print first word in list with space
    print(words[0] + " " + words[1])
    
    # Print first word in list with space
    print(words[0] + " " + words[1] + " " + words[2])
    
    # Print first word in list with space
    print(words[0] + " " + words[1] + " " + words[2] + " " + words[3])
    
    # Print first word in list with space
    print(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4])
    
    # Print first word in list with space
    print(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5])
    
    # Print first word in list with space
    print(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6])
    
    # Print first word in list with space
    print(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6] + " " + words[7])
    
    # Print first word in list with space
    print(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6] + " " + words[7] + "\n")
    
