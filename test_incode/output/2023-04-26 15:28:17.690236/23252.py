#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <filename>' % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as file:
        lines = file.readlines()
        
    words_to_remove = []
    for line in lines:
        line = line.strip()
        
        if line.find('#') != -1:
            continue
        
        if line.find(' ') != -1:
            words_to_remove.append(line)
        else:
            print('%s: line %s contains invalid characters: %s' % (filename, line, line))
    
    words_to_remove = '\n'.join(words_to_remove)
    
    with open(filename, 'w') as file:
        file.write(words_to_remove)
    
    print('Removed %d words from %s' % (len(words_to_remove), filename))
    
