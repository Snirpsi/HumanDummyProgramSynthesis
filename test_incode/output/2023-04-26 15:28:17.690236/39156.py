#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports and iterates over all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        
        port_name = port[0]
        
        print("Port name:", port_name)
        
        for port_info in port[1]:
            
            port_name = port_info[0]
            
            print("  Port name:", port_name)
            
            for port_info in port_info[1]:
                
                port_name = port_info[0]
                
                print("    ", port_name)
                
                for port_info in port_info[1]:
                    
                    port_name = port_info[0]
                    
                    print("      ", port_name)
                    
                    for port_info in port_info[1]:
                        
                        port_name = port_info[0]
                        
                        print("        ", port_name)
                        
                        for port_info in port_info[1]:
                            
                            port_name = port_info[0]
                            
                            print("          ", port_name)
                            
                            for port_info in port_info[1]:
                                
                                port_name = port_info[0]
                                
                                print("            ", port_name)
                                
                                for port_info in port_info[1]:
                                    
                                    port_name = port_info[0]
                                    
                                    print("              ", port_name)
                                    
                                    for port_info in port_info[1]:
                                        
                                        port_name = port_info[0]
                                        
                                        print("                ", port_name)
                                        
                                        for port_info in port_info[1]:
                                            
                                            port_name = port_info[0]
                                            
                                            print("                  ", port_name)
                                            
                                            for port_info in port_info[1]:
                                                
                                                port_name = port_info[0]
                                                
                                                print("                    ", port_name)
                                                
                                                for port_info in port_info[1]:
                                                    
                                                    port_name = port_info[0]
                                                    
                                                    print("                      ", port_name)
                                                    
                                                    for port_info in port_info[1]:
                                                        
                                                        port_name = port_info[0]
                                                        
                                                        print("                        ", port_name)
                                                        
                                                        for port_info in port_info[1]:
                                                            
                                                            port_name = port_info[0]
                                                            
                                                            print("                          ", port_name)
                                                            
                                                            for port_info in port_info[1]:
                                                                
                                                                port_name = port_info[0]
                                                                
                                                                print("                            ", port_name)
                                                                
                                                                for port_info in port_info[1]:
                                                                    
                                                                    port_name = port_info[0]
                                                                    
                                                                    print("                              ", port_name)
                                                                    
                                                                    for port_info in port_info[1]:
                                                                        
                                                                        port_name = port_info[0]
                                                                        
                                                                        print("                            ", port_name)
                                                                        
                                                                        for port_info in port_info