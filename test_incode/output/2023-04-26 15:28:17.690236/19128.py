#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or removes words. """    
    while True:
        word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        print(word)
        
        if word == 'quit':
            break
            
        if word in '0123456789':
            