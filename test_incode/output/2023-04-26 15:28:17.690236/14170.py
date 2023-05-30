#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers and converts all ports. """    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port < 1 or port > 65535:
            print("Error: port must be between 1 and 65535")
            sys.exit(1)
        
        if port > 0 and port < 65535:
            
            port = str(port)
            
            if port == "1":
                
                print("Removing port 1")
                
            elif port == "2":
                
                print("Removing port 2")
                
            elif port == "3":
                
                print("Removing port 3")
                
            elif port == "4":
                
                print("Removing port 4")
                
            elif port == "5":
                
                print("Removing port 5")
                
            elif port == "6":
                
                print("Removing port 6")
                
            elif port == "7":
                
                print("Removing port 7")
                
            elif port == "8":
                
                print("Removing port 8")
                
            elif port == "9":
                
                print("Removing port 9")
                
            elif port == "10":
                
                print("Removing port 10")
                
            elif port == "11":
                
                print("Removing port 11")
                
            elif port == "12":
                
                print("Removing port 12")
                
            elif port == "13":
                
                print("Removing port 13")
                
            elif port == "14":
                
                print("Removing port 14")
                
            elif port == "15":
                
                print("Removing port 15")
                
            elif port == "16":
                
                print("Removing port 16")
                
            elif port == "17":
                
                print("Removing port 17")
                
            elif port == "18":
                
                print("Removing port 18")
                
            elif port == "19":
                
                print("Removing port 19")
                
            elif port == "20":
                
                print("Removing port 20")
                
            elif port == "21":
                
                print("Removing port 21")
                
            elif port == "22":
                
                print("Removing port 22")
                
            elif port == "23":
                
                print("Removing port 23")
                
            elif port == "24":
                
                print("Removing port 24")
                
            elif port == "25":
                
                print("Removing port 25")
                
            elif port == "26":
                
                print("Removing port 26")
                
            elif port 