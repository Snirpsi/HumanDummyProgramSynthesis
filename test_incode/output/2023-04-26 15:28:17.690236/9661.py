#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers and multiplyes a port. """    
    port = int(input("Enter a port number: "))
    multiplier = int(input("Enter a multiplier: "))
    
    for num in range(1,port+1):
        print("The number is", num, "multiplied by ", multiplier)
        multiplier = multiplier * num
    
    print("The number is", port, "multiplied by ", multiplier)
    
