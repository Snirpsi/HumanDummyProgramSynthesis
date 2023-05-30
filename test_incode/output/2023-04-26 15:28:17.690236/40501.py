#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and calculates words. """    
    numbers = [int(i) for i in open('numbers.txt').read().split()]
    words = [