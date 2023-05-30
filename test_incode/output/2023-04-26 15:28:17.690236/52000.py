#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or converts a port. """    
    while True:
        port = input('Enter a port number: ')
        
        if port == 'exit':
            print('Exiting program.')
            break
        else:
            print('Converting port {} to ASCII.'.format(port))
            ascii_number = convert_port(port)
            print('ASCII number is: {}'.format(ascii_number))
            
