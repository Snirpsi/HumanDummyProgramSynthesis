#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words and opens numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        
        number = int(input('Enter a number: '))
        if number > 9 and number < 99:
            numbers.append(number)
        else:
            print('Invalid number')
            
    print('The words are:')
    for word in words:
        print(word)
    print('The numbers are:')
    for number in numbers:
        print(number)
        
    print('The word "quit" was entered.')
    
