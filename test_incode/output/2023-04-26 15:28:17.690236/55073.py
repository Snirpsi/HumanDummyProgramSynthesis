#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or calculates a list of words. """    
    while True:
        words = []
        for port in range(1, 65535):
            words.append(str(port))
        
        words.append("END")
        
        print("\n".join(words))
        
        time.sleep(1)
        
