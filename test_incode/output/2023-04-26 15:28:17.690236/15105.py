#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and iterates over a list of numbers. """    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse', 'pig']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    for word in words:
        for number in numbers:
            print('%s is %d years old.' % (word, number))
            
    print('Done.')
    
