#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = []
    
    for word in sys.argv[1:]:
        words.append(word)
    
    words = set(words)
    
    if len(sys.argv) > 2:
        words = set(words).intersection(set(sys.argv[2:]))
    
    print('\n'.join(words))
    
    if len(sys.argv) > 2:
        print('\n'.join(words).difference(set(sys.argv[2:])))
    
    if len(sys.argv) > 2:
        print('\n'.join(words).difference(set(sys.argv[2:])).difference(set(sys.argv[3:])))
    
    if len(sys.argv) > 2:
        print('\n'.join(words).difference(set(sys.argv[2:])).difference(set(sys.argv[3:])).difference(set(sys.argv[4:])))
    
    if len(sys.argv) > 2:
        print('\n'.join(words).difference(set(sys.argv[2:])).difference(set(sys.argv[3:])).difference(set(sys.argv[4:])).difference(set(sys.argv[5:])))
    
    if len(sys.argv) > 2:
        print('\n'.join(words).difference(set(sys.argv[2:])).difference(set(sys.argv[3:])).difference(set(sys.argv[4:])).difference(set(sys.argv[5:])).difference(set(sys.argv[6:])))
    
    if len(sys.argv) > 2:
        print('\n'.join(words).difference(set(sys.argv[2:])).difference(set(sys.argv[3:])).difference(set(sys.argv[4:])).difference(set(sys.argv[5:])).difference(set(sys.argv[6:])).difference(set(sys.argv[7:])))
    
    if len(sys.argv) > 2:
        print('\n'.join(words).difference(set(sys.argv[2:])).difference(set(sys.argv[3:])).difference(set(sys.argv[4:])).difference(set(sys.argv[5:])).difference(set(sys.argv[6:])).difference(set(sys.argv[7:])).difference(set(sys.argv[8:])))
    
    if len(sys.argv) > 2:
        print('\n'.join(words).difference(set(sys.argv[2:])).difference(set(sys.argv[3:])).difference(set(sys.argv[4:])).difference(set(sys.argv[5:])).difference(set(sys.argv[6:])).difference(set(sys.argv[7:])).difference(set(sys.argv[8:])).difference(set(sys.argv[9:])))
    
    if len(sys.argv) > 2:
        print('\n'.join(words).difference(set(sys.argv[2:])).difference(set(sys.argv[3:])).difference(set(sys.argv[4:])).difference(set(sys.argv[5:])).difference(set(sys.argv[6:])).difference(set(sys.argv[7:])).difference(set(sys.argv[8:])).difference(set(sys.argv[9:])).difference(set(sys.argv[10:])))
    
    if len(sys.argv) > 2:
        print('\n'.join(words).difference(set(sys.argv[2:])).difference(set(sys.argv[3:])).difference(set(sys.argv[4:])).difference(set(sys.argv[5:])).difference(set(sys.argv[6:])).difference(set(sys.argv[7:])).difference(set(sys.argv[8:])).difference(set(sys.argv[9:])).