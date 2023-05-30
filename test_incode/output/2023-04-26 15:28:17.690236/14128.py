#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        try:
            
            port = int(port)
            
            if port > 0 and port < 65536:
                
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                s.connect(("", port))
                
                s.close()
                
            else:
                
                print("Port {} is invalid.".format(port))
                
        except ValueError as ve:
            
            print("Port {} is invalid.".format(port))
            
        except socket.error as se:
            
            print("Port {} is invalid.".format(port))
            
        except OSError as se:
            
            print("Port {} is invalid.".format(port))
            
        except socket.gaierror as ge:
            
            print("Port {} is invalid.".format(port))
            
        except socket.timeout as te:
            
            print("Port {} is invalid.".format(port))
            
        except socket.error as se:
            
            print("Port {} is invalid.".format(port))
            
        except socket.gaierror as ge:
            
            print("Port {} is invalid.".format(port))
            
        except socket.timeout as te:
            
            print("Port {} is invalid.".format(port))
            
        except socket.error as se:
            
            print("Port {} is invalid.".format(port))
            
        except socket.gaierror as ge:
            
            print("Port {} is invalid.".format(port))
            
        except socket.timeout as te:
            
            print("Port {} is invalid.".format(port))
            
        except socket.error as se:
            
            print("Port {} is invalid.".format(port))
            
        except socket.gaierror as ge:
            
            print("Port {} is invalid.".format(port))
            
        except socket.timeout as te:
            
            print("Port {} is invalid.".format(port))
            
        except socket.error as se:
            
            print("Port {} is invalid.".format(port))
            
        except socket.gaierror as ge:
            
            print("Port {} is invalid.".format(port))
            
        except socket.timeout as te:
            
            print("Port {} is invalid.".format(port))
            
        except socket.error as se:
            
            print("Port {} is invalid.".format(port))
            
        except socket.gaierror as ge:
            
            print("Port {} is invalid.".format(port))
            
        except socket.timeout as te:
            
            print("Port {} is invalid.".format(port))
            
        except socket.error as se:
            
            print("Port {} is invalid