#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['cat', 'dog', 'mouse', 'chicken', 'elephant', 'bird', 'cat', 'dog', 'mouse', 'chicken', 'elephant', 'bird']
    
    while True:
        words = words + ['cat', 'dog', 'mouse', 'chicken', 'elephant', 'bird']
        
        for word in words:
            print(word)
            
        choice = input('\nDo you want to continue (y/n)?')
        
        if choice == 'y':
            break
        elif choice == 'n':
            break
        else:
            print('Invalid input')
            
    print('Done')
    
