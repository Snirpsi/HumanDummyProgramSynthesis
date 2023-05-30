#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and stores a list of numbers. """    
    
    fruits = []
    
    # Add fruits to the list 
    fruits.append(1)
    fruits.append(2)
    fruits.append(3)
    
    # Print the list 
    print('Fruits:', fruits)
    
    # Start the webserver 
    httpd = HTTPServer(('', 80), FruitServer)
    
    # Start the webserver 
    httpd.serve_forever()
    
