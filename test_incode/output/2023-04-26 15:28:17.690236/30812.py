#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['apple', 'banana', 'cherry']
    
    while True:
        print('The words are:')
        for word in words:
            print(word)
        
        choice = input('Do you want to add another word? Y/N: ')
        
        if choice == 'Y' or choice == 'y':
            words.append(input('Enter a word: '))
        else:
            print('Goodbye!')
            break
    
    print('The words are:')
    for word in words:
        print(word)
    
    print('Goodbye!')
    
