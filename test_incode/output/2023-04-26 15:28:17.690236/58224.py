#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and removes all ports. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that removes a list of words and removes all ports.')
    parser.add_argument('words', metavar='words', type=str, nargs='+', help='The words to remove.')
    parser.add_argument('-p', '--port', type=int, default=8000, help='The port to listen on.')
    args = parser.parse_args()
    
    # Remove all words and ports
    remove_words(args.words, args.port)
    
