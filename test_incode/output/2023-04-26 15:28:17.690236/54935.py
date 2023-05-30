#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    while True:
        for word in words:
            print(word)
        
        choice = input("Press enter to continue: ")
        if choice == '':
            break
        
