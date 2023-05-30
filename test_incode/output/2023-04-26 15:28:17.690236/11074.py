#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        
        if word in words:
            print(word)
        else:
            print('That word is not in the list')
            
    print('Goodbye')
