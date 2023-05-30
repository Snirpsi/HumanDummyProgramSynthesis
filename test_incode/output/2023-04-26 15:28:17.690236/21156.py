#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers and adds fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    while True:
        for fruit in fruits:
            for number in numbers:
                print('{} {}'.format(number, fruit))
                time.sleep(