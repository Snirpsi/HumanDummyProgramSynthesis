#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers and adds fruits. """    
    
    port = int(sys.argv[1])
    
    numbers = range(1,11)
    fruits = ['apple', 'orange', 'pear', 'banana', 'grape', 'mango', 'cherry', 'pineapple', 'peach']
    
    server = HTTPServer(('', port), FruitServer)
    
    server.serve_forever()
    
