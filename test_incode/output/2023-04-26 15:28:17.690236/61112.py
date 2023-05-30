#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and stores user input. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word == '':
            print('No word was entered. Try again.')
            continue
        
        words.append(word)
    
    print('Words:')
    
    for word in words:
        print(word)
    
    print('')
    
    print('Enter a number to quit or 0 to continue:')
    
    choice = int(input('Enter a number: '))
    
    if choice == 0:
        print('Goodbye!')
        
