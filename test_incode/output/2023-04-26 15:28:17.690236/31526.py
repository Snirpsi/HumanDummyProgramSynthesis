#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or prints words. """    
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'user':
            print('Username:')
            
            username = input('Username: ')
            
            print('Password:')
            
            password = input('Password: ')
            
            print('Welcome ' + username + '!')
            
            print('Your password is: ' + password)
            
        elif sys.argv[1] == 'words':
            print('Words:')
            
            words = input('Words: ')
            
            print('\n'.join(words))
            
        else:
            print('Wrong command!')
    else:
        print('Usage: python3 words.py')
        
