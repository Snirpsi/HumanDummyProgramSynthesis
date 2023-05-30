#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or enumerates numbers. """    
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Print usage message and exit
    if len(args) != 1:
        print("Usage: %s [word|number]" % sys.argv[0])
        sys.exit(1)
    
    # Parse argument and convert it to an int
    argument = args[0]
    if argument == "word":
        number = 1
    elif argument == "number":
        number = int(argument)
    else:
        print("Invalid argument: %s" % argument)
        sys.exit(1)
    
    # Print the result
    print("%d %s" % (number, words[number]))
    
