#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers and converts words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    numbers = []
    
    while True:
        number = int(input('Enter a number: '))
        if number == 999:
            break
        numbers.append(number)
    
    numbers = list(map(str, numbers))
    
    for number in numbers:
        word = words[number % 10]
        print('{} {}'.format(number, word))
        
