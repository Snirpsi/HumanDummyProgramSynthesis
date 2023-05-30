#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or opens a list of numbers. """    
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('words', nargs='*', help='words to convert')
    parser.add_argument('numbers', nargs='*', help='numbers to convert')
    args = parser.parse_args()
    
    words = []
    numbers = []
    if args.words:
        words = [w.strip() for w in args.words]
    if args.numbers:
        numbers = [n.strip() for n in args.numbers]
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    numbers = numbers if numbers else []
    words = words if words else []
    
    