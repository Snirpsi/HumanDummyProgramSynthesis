#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words. """    
    while True:
        words = []
        with open('words.txt') as f:
            for line in f:
                line = line.strip()
                words.append(line)
        
        for word in words:
            print(word)
            
        time.sleep(1)
        
