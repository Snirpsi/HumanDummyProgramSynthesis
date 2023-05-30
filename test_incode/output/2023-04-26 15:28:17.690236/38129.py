#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or opens words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'words'
        
    words = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line != '':
                words.append(line)
    
    words.sort()
    
    sys.stdout.write('\n'.join(words))
    
    sys.stdout.write('\n')
    
    sys.stdout.write('Open words in your browser: ')
    
    webbrowser.open('http://127.0.0.1:8000')
    
    sys.stdout.write('\n')
    
    sys.stdout.write('Press Ctrl+C to quit.\n')
    
    sys.stdout.flush()
    
    