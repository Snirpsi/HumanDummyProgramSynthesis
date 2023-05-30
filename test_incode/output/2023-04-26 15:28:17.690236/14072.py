#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <input>' % sys.argv[0])
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename) as input_file:
        lines = input_file.readlines()
    
    lines = map(lambda x: x.strip(), lines)
    
    lines = map(lambda x: x.replace('\n', ''), lines)
    
    lines = map(lambda x: x.replace('\t', ''), lines)
    
    lines = map(lambda x: x.replace('\r', ''), lines)
    
    lines = map(lambda x: x.replace('"', ''), lines)
    
    lines = map(lambda x: x.replace('\'', ''), lines)
    
    lines = map(lambda x: x.replace('\\', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(',', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
    lines = map(lambda x: x.replace(':', ''), lines)
    
    lines = map(lambda x: x.replace(';', ''), lines)
    
