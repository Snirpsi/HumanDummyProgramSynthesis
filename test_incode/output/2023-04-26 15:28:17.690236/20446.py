#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and converts a port. """    
    
    port = '/dev/ttyUSB0'
    
    portnum = port.rfind(':')
    
    if portnum == -1:
        print('Port number not found')
        
    else:
        print('Port number found')
        
        portnum = portnum + 1
        
        port = port[0:portnum]
        
        portnum = port.rfind(':')
        
        if portnum == -1:
            print('Port number not found')
            
        else:
            print('Port number found')
            
            portnum = portnum + 1
            
            port = port[0:portnum]
            
            portnum = port.rfind(':')
            
            if portnum == -1:
                print('Port number not found')
                
            else:
                print('Port number found')
                
                portnum = portnum + 1
                
                port = port[0:portnum]
                
                portnum = port.rfind(':')
                
                if portnum == -1:
                    print('Port number not found')
                    
                else:
                    print('Port number found')
                    
                    portnum = portnum + 1
                    
                    port = port[0:portnum]
                    
                    portnum = port.rfind(':')
                    
                    if portnum == -1:
                        print('Port number not found')
                        
                    else:
                        print('Port number found')
                        
                        portnum = portnum + 1
                        
                        port = port[0:portnum]
                        
                        portnum = port.rfind(':')
                        
                        if portnum == -1:
                            print('Port number not found')
                            
                        else:
                            print('Port number found')
                            
                            portnum = portnum + 1
                            
                            port = port[0:portnum]
                            
                            portnum = port.rfind(':')
                            
                            if portnum == -1:
                                print('Port number not found')
                                
                            else:
                                print('Port number found')
                                
                                portnum = portnum + 1
                                
                                port = port[0:portnum]
                                
                                portnum = port.rfind(':')
                                
                                if portnum == -1:
                                    print('Port number not found')
                                
                                else:
                                    print('Port number found')
                                
                                    portnum = portnum + 1
                                    
                                    port = port[0:portnum]
                                    
                                    portnum = port.rfind(':')
                                    
                                    if portnum == -1:
                                        print('Port number not found')
                                    
                                    else:
                                        print('Port number found')
                                        
                                        portnum = portnum + 1
                                        
                                        port = port[0:portnum]
                                        
                                        portnum = port.rfind(':')
                                        
                                        if portnum == -1:
