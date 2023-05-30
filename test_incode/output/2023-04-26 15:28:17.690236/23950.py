#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words and enumerates numbers. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'snake', 'bird', 'cat', 'dog', 'mouse', 'bird', 'snake', 'bird']
    
    numbers = []
    
    while True:
        number = input('Enter a number: ')
        if number in words:
            numbers.append(number)
        else:
            print('That number is not in the list')
    
    print('The numbers are:')
    for number in numbers:
        print(number)
        
    print('Goodbye!')
    
