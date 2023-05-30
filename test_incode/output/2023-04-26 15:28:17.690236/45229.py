#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['apple', 'banana', 'cherry']
    
    while True:
        print('Multiplying {} by {} yields:'.format(*words))
        print(*map(lambda x: x * words[0], words))
        
        time.sleep(1)
        
        
