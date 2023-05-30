#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['foo', 'bar', 'baz', 'qux']
    
    while True:
        for word in words:
            print(word)
        
        choice = input('Press enter to exit: ')
        if choice == '':
            break
        else:
            words.remove(choice)
    
    print('Done!')
    
