#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits or converts a port. """    
    port = int(sys.argv[1])
    fruit = sys.argv[1]
    
    if fruit == "fruit":
        fruit = Fruit()
        fruit.open()
    elif fruit == "fruits":
        fruit = Fruits()
        fruit.open()
    else:
        print("Invalid fruit type.")
        
    fruit.close()
    
