#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports and iterates over a list of words. """    
    
    ports = range(1,65535)
    words = ['a', 'b', 'c']
    
    while True:
        
        for port in ports:
            
            word = ''.join(random.choice(words) for i in range(port))
            
            print('Port {} is {}'.format(port, word))
            
            time.sleep(1)
            
        time.sleep(1)
        
