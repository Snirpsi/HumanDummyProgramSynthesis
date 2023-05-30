#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and removes a list of numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    i = 0
    while i < len(words):
        word = words[i]
        number = numbers[i]
        
        if word in numbers:
            numbers.remove(number)
            
        i += 1
        
    print('The numbers are:')
    for number in numbers:
        print(number)
    
    print('The words 