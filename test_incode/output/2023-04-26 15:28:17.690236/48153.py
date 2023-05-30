#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or converts a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <filename>' % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    numbers = []
    words = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            
            if line.startswith('#'):
                continue
            
            parts = line.split('\t')
            
            if len(parts) != 2:
                print('Invalid line format: %s' % line)
                continue
            
            numbers.append(int(parts[0]))
            words.append(parts[1])
    
    numbers = sorted(numbers)
    words = sorted(words)
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:50]
    words = words[:50]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    