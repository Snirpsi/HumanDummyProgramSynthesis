#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        for word in words:
            print(word)
        
        choice = input('Enter your choice: ')
        
        if choice == 'exit':
            break
        else:
            words.remove(choice)
    
    print('Done')
