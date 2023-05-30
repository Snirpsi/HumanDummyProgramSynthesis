#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    words = input().split()
    words = [int(x) for x in words]
    print(sum(words))
