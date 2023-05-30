#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers and stores a list of words. """    
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        numbers = []
        
        for number in range(1, 10):
            numbers.append(str(number))
        
        numbers.append(word)
        
        print('\n'.join(numbers))
        
        print('\n')
        
    print('Goodbye!')
    
