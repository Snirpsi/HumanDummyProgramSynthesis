#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    numbers = []
    words = []
    
    for line in lines:
        line = line.strip()
        
        if line.startswith('#'):
            continue
        
        parts = line.split('\t')
        
        if len(parts) != 2:
            print("Error: invalid line '%s'" % line)
            sys.exit(1)
        
        number = parts[0].strip()
        word = parts[1].strip()
        
        if number == '':
            continue
        
        numbers.append(number)
        words.append(word)
    
    numbers = sorted(numbers)
    words = sorted(words)
    
    numbers_str = '\n'.join(numbers)
    words_str = '\n'.join(words)
    
    print("Numbers:\n%s" % numbers_str)
    print("Words:\n%s" % words_str)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    