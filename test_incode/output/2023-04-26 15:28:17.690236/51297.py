#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and multiplyes all ports. """    
    
    ports = [int(i) for i in sys.argv[1:]]
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    for port in ports:
        
        fruit = ''.join(random.choice(fruits) for _ in range(port))
        
        print('serving fruit {}'.format(fruit))
        
        server = HTTPServer(("", port), FruitHandler)
        
        server.serve_forever()
        
    
