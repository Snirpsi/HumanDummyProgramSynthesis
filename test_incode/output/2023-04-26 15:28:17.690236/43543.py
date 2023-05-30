#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    words = []
    
    # Read words from stdin and write them to stdout.
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        # Strip leading and trailing whitespace.
        line = line.lstrip()
        line = line.rstrip()
        
        # Remove leading and trailing whitespace.
        line = line.lstrip()
        line = line.rstrip()
        
        # Split into words.
        words = line.split()
        
        # Write to stdout.
        print(' '.join(words))
        
    # Close the stdin stream.
    sys.stdin.close()
    
    # Write the words to stdout.
    print(' '.join(words))
    
    # Close the stdout stream.
    sys.stdout.close()
    
    # Close the stderr stream.
    sys.stderr.close()
    
    # Run the webserver.
    webserver.serve_forever()
    
