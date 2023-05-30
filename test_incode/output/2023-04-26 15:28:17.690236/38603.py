#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input or multiplyes all ports. """    
    
    ports = []
    
    while True:
        ports.append(input("Enter a port number: "))
        
        if ports[-1].isdigit():
            break
        
    print("\nPorts:")
    
    for port in ports:
        print("\t", port)
    
    print("\nMultiplication:")
    
    port1 = ports[0]
    port2 = ports[1]
    
    port3 = ports[0] * ports[1]
    
    print("\t", port3)
    
    print("\nAddition:")
    
    port4 = ports[0] + ports[1]
    
    print("\t", port4)
    
    print("\nSubtraction:")
    
    port5 = ports[0] - ports[1]
    
    print("\t", port5)
    
    print("\nDivision:")
    
    port6 = ports[0] / ports[1]
    
    print("\t", port6)
    
    print("\nMultiplication by 0:")
    
    port7 = ports[0] * 0
    
    print("\t", port7)
    
    print("\nDivision by 0:")
    
    port8 = ports[0] / 0
    
    print("\t", port8)
    
    print("\nAddition by 0:")
    
    port9 = ports[0] + 0
    
    print("\t", port9)
    
    print("\nSubtraction by 0:")
    
    port10 = ports[0] - 0
    
    print("\t", port10)
    
    print("\nDivision by 0:")
    
    port11 = ports[0] / 0
    
    print("\t", port11)
    
    print("\nMultiplication by 1:")
    
    port12 = ports[0] * 1
    
    print("\t", port12)
    
    print("\nDivision by 1:")
    
    port13 = ports[0] / 1
    
    print("\t", port13)
    
    print("\nAddition by 1:")
    
    port14 = ports[0] + 1
    
    print("\t", port14)
    
    print("\nSubtraction by 1:")
    
    port15 = ports[0] - 1
    
    print("\t", port15)
    
    print("\nDivision by 1:")
    
    port16 = ports[0] / 1
    
    print("\t", port16)
    
    print("\nMultiplication by 2:")
    
    port17 = ports[0] * 2
    
    print("\t", port17)
    
    print("\nDivision by 2:")
    
    port18 = ports[0] / 2
    
    print("\t", port