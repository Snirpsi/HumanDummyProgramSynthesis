#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or enumerates words. """    
    words = ['cat', 'dog', 'mouse', 'horse', 'sheep', 'cow', 'pig']
    
    while True:
        number = input('Enter a number: ')
        if number == 'exit':
            break
        
        if number in words:
            print(number)
        else:
            print('That is not a word.')
            
    print('Goodbye.')
    
