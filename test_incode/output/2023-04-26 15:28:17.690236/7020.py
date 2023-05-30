#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or calculates words. """    
    
    numbers = []
    words = []
    
    while True:
        try:
            number = int(input('Enter a number: '))
            numbers.append(number)
        except ValueError:
            print('Invalid input')
            continue
        
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'quit':
            break
        
    print('The numbers are: ')
    for number in numbers:
        print(number)
    
    print('The words are: ')
    for word in words:
        print(word)
        
    print('The word "quit" was found')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    