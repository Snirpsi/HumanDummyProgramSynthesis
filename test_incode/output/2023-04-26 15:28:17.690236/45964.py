#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or prints user input. """    
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('words', nargs='+', help='words to enumerate')
    args = parser.parse_args()
    
    words = [w.strip() for w in args.words]
    
    print('\n'.join(words))
    
