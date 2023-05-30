#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    # Calculate list of numbers
    numbers = []
    
    # Read numbers from stdin
    for line in sys.stdin:
        line = line.strip()
        numbers.append(int(line))
    
    # Calculate list of words
    words = [word for word in words if word.isalpha()]
    numbers = [number for number in numbers if number > 0]
    
    # Write to stdout
    sys.stdout.write('\n'.join(words))
    sys.stdout.write('\n')
    sys.stdout.write('\n'.join(str(number) for number in numbers))
    
    # Close the connection
    sys.stdout.flush()
    sys.stderr.flush()
    
    # Run the server
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
