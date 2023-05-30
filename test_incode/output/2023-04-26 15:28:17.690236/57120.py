#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words and opens user input. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    words_to_remove = []
    
    while len(words_to_remove) > 0:
        word = input('Enter a word: ')
        
        if word in words:
            words_to_remove.append(word)
            
        else:
            print('That word is not in the list')
    
    print('\nThe following words were removed:')
    
    for word in words_to_remove:
        print(word)
        
    print('\nThank you!')
    
