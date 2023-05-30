#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port or prints a list of words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        port = 8080
    else:
        port = int(sys.argv[1])
    
    webbrowser.open('http://localhost:' + str(port))
    
    print('List of words: ')
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    for word in words:
        print(word)
        
    print('\nDone.')
    
