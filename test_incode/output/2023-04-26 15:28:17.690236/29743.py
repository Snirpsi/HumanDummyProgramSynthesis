#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or multiplyes a port. """    
    while True:
        word = input('Enter a word: ')
        number = int(input('Enter a number: '))
        port = int(input('Enter a port: '))
        
        if word == 'exit':
            break
        
        if number % 2 == 0:
            port *= number
        else:
            port += number
        
        print('The port is now', port)
        
        print('The word is', word)
        
        print('The number is', number)
        
        print('The port is', port)
        
        print('Press enter to continue')
        
        input()
        
    print('Thank you for using the port-multiplier program')
    
