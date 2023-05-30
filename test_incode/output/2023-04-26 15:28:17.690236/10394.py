#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and returns a list of words. """    
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert numbers to words')
    parser.add_argument('numbers', metavar='N', type=int, nargs='+', help='numbers to convert')
    args = parser.parse_args()
    
    numbers = args.numbers
    
    words = []
    for number in numbers:
        words.append(str(number))
        
    print('\n'.join(words))
    
