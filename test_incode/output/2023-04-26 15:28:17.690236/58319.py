#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and adds a list of numbers. """    
    
    port = int(sys.argv[1])
    
    numbers = []
    
    # Iterate over all numbers and add them to the list
    for i in range(port):
        numbers.append(i)
    
    # Print the list
    print(numbers)
    
    # Start the webserver
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Run the webserver
    httpd.serve_forever()
    
