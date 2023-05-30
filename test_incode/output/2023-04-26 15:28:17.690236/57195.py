#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and adds all ports. """    
    
    ports = [8080, 8081, 8082]
    
    words = ['hello', 'world']
    
    ports_sum = 0
    
    for port in ports:
        
        words_sum = 0
        
        for word in words:
            
            words_sum += word
            
        ports_sum += port
        
        print('Port {} is {}'.format(port, words_sum))
    
    print('The sum of the ports is {}'.format(ports_sum))
    
