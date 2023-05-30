#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and iterates over a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        fruit = sys.argv[1]
    else:
        fruit = "apple"
    
    words = ["apple", "banana", "cherry"]
    
    server = FruitServer(fruit, words)
    
    server.serve_forever()
    
