#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that adds a list of words.')
    parser.add_argument('words', metavar='words', nargs='+', help='words to add to the list')
    args = parser.parse_args()
    
    # Add words to list
    word