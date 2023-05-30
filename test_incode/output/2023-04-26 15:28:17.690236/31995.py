#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
        
    print('The words are:')
    
    for word in words:
        print(word)
        
    print('\nThe word "end" is in the middle of the list')
    
    if words[-1] == 'end':
        print('The word "end" is in the middle of the list')
        
    print('\nThe word "end" is at the end')
    
    if words[-2] == 'end':
        print('The word "end" is at the end')
        
    print('\nThe word "end" is at the beginning')
    
    if words[0] == 'end':
        print('The word "end" is at the beginning')
        
    print('\nThe word "end" is at the end')
    
    if words[-2] == 'end':
        print('The word "end" is at the end')
        
    print('\nThe word "end" is at the beginning')
    
    if words[0] == 'end':
        print('The word "end" is at the beginning')
        
    print('\nThe word "end" is at the end')
    
    if words[-2] == 'end':
        print('The word "end" is at the end')
        
    print('\nThe word "end" is at the beginning')
    
    if words[0] == 'end':
        print('The word "end" is at the beginning')
        
    print('\nThe word "end" is at the end')
    
    if words[-2] == 'end':
        print('The word "end" is at the end')
        
    print('\nThe word "end" is at the beginning')
    
    if words[0] == 'end':
        print('The word "end" is at the beginning')
        
    print('\nThe word "end" is at the end')
    
    if words[-2] == 'end':
        print('The word "end" is at the end')
        
    print('\nThe word "end" is at the beginning')
    
    if words[0] == 'end':
        print('The word "end" is at the beginning')
        
    print('\nThe word "end" is at the end')
    
    if words[-2] == 'end':
        print('The word "end" is at the end')
        
    print('\nThe word "end" is at the beginning')
    
    if words[0] == 'end':
        print('The word "end" is at the beginning')
        
    print('\nThe word "end" is at the end')
    
    if words[-2] == 'end':
        print('The word "end" is at the end')