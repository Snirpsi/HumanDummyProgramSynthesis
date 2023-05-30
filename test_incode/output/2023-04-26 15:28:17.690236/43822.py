#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['apple', 'banana', 'cherry']
    while True:
        print('\nAdding words...')
        for word in words:
            print('  ', word)
        
        choice = input('\nChoose an option: ')
        if choice == 'quit':
            break
        else:
            words.append(choice)
            print('  ', choice)
        
    print('\nDone!')
    
