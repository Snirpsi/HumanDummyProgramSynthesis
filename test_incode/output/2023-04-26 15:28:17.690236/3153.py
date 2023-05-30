#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        
        lines = file.readlines()
        
        words = []
        
        for line in lines:
            
            line = line.strip()
            
            if len(line) == 0:
                continue
            
            words = words + line.split(' ')
            
        words = words + ['']
        
        words = list(set(words))
        
        words = list(filter(lambda x: len(x) > 0, words))
        
        words = list(filter(lambda x: len(x) <= 3, words))
        
        words = list(filter(lambda x: len(x) == 3, words))
        
        words = list(filter(lambda x: len(x) == 4, words))
        
        words = list(filter(lambda x: len(x) == 5, words))
        
        words = list(filter(lambda x: len(x) == 6, words))
        
        words = list(filter(lambda x: len(x) == 7, words))
        
        words = list(filter(lambda x: len(x) == 8, words))
        
        words = list(filter(lambda x: len(x) == 9, words))
        
        words = list(filter(lambda x: len(x) == 10, words))
        
        words = list(filter(lambda x: len(x) == 11, words))
        
        words = list(filter(lambda x: len(x) == 12, words))
        
        words = list(filter(lambda x: len(x) == 13, words))
        
        words = list(filter(lambda x: len(x) == 14, words))
        
        words = list(filter(lambda x: len(x) == 15, words))
        
        words = list(filter(lambda x: len(x) == 16, words))
        
        words = list(filter(lambda x: len(x) == 17, words))
        
        words = list(filter(lambda x: len(x) == 18, words))
        
        words = list(filter(lambda x: len(x) == 19, words))
        
        words = list(filter(lambda x: len(x) == 20, words))
        
        words = list(filter(lambda x: len(x) == 21, words))
        
        words = list(filter(lambda x: len(x) == 22, words))
        
        words = list(filter(lambda x: len(x) == 23, words))
        
        words = list(filter(lambda x: len(x) == 24, words))
        
        words = list(filter(lambda x: len(x) == 25, words))
        
        words = list(filter(lambda x: len(x) == 26, words))
        
        words = list(filter(lambda x: len(x) == 27, words))
        
        words = list(filter(lambda x: len(x) == 28, words))
        
        words = list(filter(lambda x: len(x) == 29, words))
        
        words = list(filter(lambda x: len(