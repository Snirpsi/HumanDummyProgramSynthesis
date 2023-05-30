#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits or calculates a list of words. """    
    
    # Load and parse config file
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    
    # Load and parse command line arguments
    args = sys.argv[1:]
    
    # Parse command line arguments
    for arg in args:
        if arg == '-h':
            print('Usage: %s [options]' % sys.argv[0])
            sys.exit()
        elif arg == '--help':
            print('Usage: %s [options]' % sys.argv[0])
            sys.exit()
        elif arg == '--version':
            print('Usage: %s [options]' % sys.argv[0])
            sys.exit()
        elif arg == '--fruits':
            fruits = load_fruits(config)
            print_fruits(fruits)
        elif arg == '--words':
            words = load_words(config)
            print_words(words)
        else:
            print('Error: unknown argument: %s' % arg)
            sys.exit()
