#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or returns a list of words. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that iterates over user input or returns a list of words.')
    parser.add_argument('-c', '--count', metavar='COUNT', type=int, help='The number of words to return.')
    parser.add_argument('-n', '--number', metavar='NUMBER', type=int, help='The number of words to return.')
    parser.add_argument('-r', '--reverse', metavar='REVERSE', action='store_true', help='Reverse the words in the list.')
    parser.add_argument('-l', '--list', metavar='LIST', nargs='*', help='The words to return.')
    parser.add_argument('-p', '--port', metavar='PORT', type=int, help='The port to listen on.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output.')
    args = parser.parse_args()
    
    # Get the number of words to return
    if args.count:
        count = args.count
    else:
        count = 100
    
    # Get the number of words to return
    if args.number:
        number = args.number
    else:
        number = 10
    
    # Get the number of words to return
    if args.reverse:
        reverse = True
    else:
        reverse = False
    
    # Get the number of words to return
    if args.list:
        words = args.list
    else:
        words = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']
    
    # Get the number of words to return
    if args.port:
        port = args.port
    else:
        port = 8000
    
    # Get the number of words to return
    if args.verbose:
        verbose = True
    else:
        verbose = False
    
    # Run the server
    run(count, number, reverse, words, port, verbose)
    
