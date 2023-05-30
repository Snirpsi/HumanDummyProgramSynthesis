#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port or stores a list of words. """    
    while True:
        port = input('Enter a port number: ')
        words = []
        
        if port == '':
            print('No port number given')
        else:
            print('Listing words for port ' + port)
            
            words = list(''.join(open('words.txt').readlines()))
            
            print('\n'.join([word for word in words if word != port]))
            
            print('\n'.join([word for word in words if port in word]))
            
            print('\n'.join([word for word in words if port not in word]))
            
            print('\n'.join([word for word in words if port in word and word != port]))
            
            print('\n'.join([word for word in words if port not in word and word != port]))
            
            print('\n'.join([word for word in words if port in word and port not in word]))
            
            print('\n'.join([word for word in words if port not in word and port not in word]))
            
            print('\n'.join([word for word in words if port in word and port in word]))
            
            print('\n'.join([word for word in words if port not in word and port in word]))
            
            print('\n'.join([word for word in words if port not in word and port not in word]))
            
            print('\n'.join([word for word in words if port in word and port not in word]))
            
            print('\n'.join([word for word in words if port not in word and port not in word]))
            
            print('\n'.join([word for word in words if port in word and port not in word]))
            
            print('\n'.join([word for word in words if port not in word and port not in word]))
            
            print('\n'.join([word for word in words if port in word and port not in word]))
            
            print('\n'.join([word for word in words if port not in word and port not in word]))
            
            print('\n'.join([word for word in words if port in word and port not in word]))
            
            print('\n'.join([word for word in words if port not in word and port not in word]))
            
            print('\n'.join([word for word in words if port in word and port not in word]))
            
            print('\n'.join([word for word in words if port not in word and port not in word]))
            
            print('\n'.join([word for word in words if port in word and port not in word]))
            
            print('\n'.join([word for word in words if port not in word and port not in word]))
            
            print('\n'.join([word for word in words if port in word and port not in word]))
            
            print('\n'.join([word for word in words if port not in word and port not in word]))
            
            print('\n'.join([word for word in words if port in 