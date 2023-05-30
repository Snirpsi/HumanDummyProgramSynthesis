#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    
    # Read words from stdin
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        words.append(line)
    
    # Write words to stdout
    sys.stdout.write('\n'.join(words))
    
    # Close stdin
    sys.stdin.close()
    
    # Close stdout
    sys.stdout.close()
    
    # Close stderr
    sys.stderr.close()
    
    # Return 