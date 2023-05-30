#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0])
        sys.exit()
    
    for filename in sys.argv[1:]:
        with open(filename) as f:
            lines = f.readlines()
            
        numbers = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            number = int(line)
            if number in numbers:
                numbers.remove(number)
            else:
                numbers.append(number)
            
        with open(filename, 'w') as f:
            for line in numbers:
                f.write(str(line) + '\n')
    
