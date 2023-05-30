#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input and enumerates a list of words. """    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'q':
            break
        
        print('The word "{}" was added to the list.'.format(word))
        
    print('The list contains:')
    for word in words:
        print('"{}".'.format(word))
        
    print('\nThe word "q" was 