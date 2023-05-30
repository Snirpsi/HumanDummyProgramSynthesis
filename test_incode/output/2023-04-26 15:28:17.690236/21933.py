#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and returns fruits. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    fruits = []
    for p in ports:
        fruits.append(get_fruit(p))
    
    print(json.dumps(fruits, indent=4))

<|/ file ext=.py source=github |>