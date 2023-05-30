#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and enumerates numbers. """    
    
    words = []
    numbers = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        numbers.append(int(word))
        words.append(word)
        
    print('Words:', words)
    print('Numbers:', numbers)
    
    print('\nThe word that occurs most often is "{}"'.format(
        max(numbers, key=numbers.count)))
    
    print('\nThe word that occurs least often is "{}"'.format(
        min(numbers, key=numbers.count)))
    
    print('\nThe number that occurs most often is {}'.format(
        max(numbers, key=numbers.count)))
    
    print('\nThe number that occurs least often is {}'.format(
        min(numbers, key=numbers.count)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    