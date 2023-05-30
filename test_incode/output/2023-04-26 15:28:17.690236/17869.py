#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers and enumerates words. """    
    numbers = [1,2,3,4,5,6,7,8,9,0]
    words = ['one','two','three','four','five','six','seven','eight','nine','ten']
    
    for index, num in enumerate(numbers):
        print('The number {} is {}.'.format(num, words[index]))
    
    # Write your code 