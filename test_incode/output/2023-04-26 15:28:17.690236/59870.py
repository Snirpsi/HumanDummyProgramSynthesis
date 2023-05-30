#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers and multiplyes a list of numbers. """    
    port = int(sys.argv[1])
    
    numbers = []
    
    # Add numbers to the list
    for i in range(10):
        numbers.append(i)
        
    # Multiply all numbers in the list
    for i in range(10):
        numbers[i] *= i
        
    # Display all numbers
    for i in range(10):
        print(numbers[i])
        
    # Start server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start webserver
    httpd.serve_forever()
    
