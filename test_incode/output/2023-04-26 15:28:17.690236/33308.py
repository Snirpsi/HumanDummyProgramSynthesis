#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words or opens numbers. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: %s <file> <word>' % sys.argv[0])
        exit(1)
    
    file = sys.argv[1]
    word = sys.argv[2]
    
    file = open(file, 'r')
    
    words = file.read().split()
    
    file.close()
    
    words = [word for word in words if word not in words]
    
    file = open(file, 'w')
    
    file.write('\n'.join(words))
    
    file.close()
    
    print('Removed %s and added %s' % (word, file))
    
    
