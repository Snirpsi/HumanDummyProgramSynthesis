#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['hello', 'world', 'how', 'are', 'you', 'today']
    
    while True:
        answer = words[0] * words[1] * words[2] * words[3] * words[4] * words[5] * words[6] * words[7] * words[8] * words[9]
        
        print('Answer is:', answer)
        
        time.sleep(1)
        
