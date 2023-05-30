#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports and iterates over user input. """    
    
    ports = input("Enter ports separated by comma: ").split(',')
    
    for port in ports:
        
        port_number = int(port)
        
        if port_number > 65535:
            print("Port number must be less than 65535")
        elif port_number < 1:
            print("Port number must be greater than 1")
        else:
            
            ports_to_convert = []
            
            for port in ports:
                
                port_number = int(port)
                
                if port_number > 65535:
                    print("Port number must be less than 65535")
                elif port_number < 1:
                    print("Port number must be greater than 1")
                else:
                    ports_to_convert.append(port_number)
            
            ports_to_convert = list(set(ports_to_convert))
            
            ports_to_convert.sort()
            
            ports_to_convert = ports_to_convert[::-1]
            
            for port_number in ports_to_convert:
                
                port_name = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
                print("Port number " + str(port_number) + ": " + port_name)
                
                port_number = str(port_number)
                
