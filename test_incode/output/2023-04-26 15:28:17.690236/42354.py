#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    
    # read a list of numbers from stdin
    numbers = map(int, sys.stdin.readline().split())
    
    # remove all numbers from list
    numbers = filter(lambda x: x not in numbers, numbers)
    
    # write results to stdout
    sys.stdout.write('\n'.join(map(str, numbers)))
    
    # exit with return code 0
    sys.exit(0)
