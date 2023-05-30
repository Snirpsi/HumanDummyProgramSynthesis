#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or opens a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1]
        
    else:
        ports = input("Enter ports separated by comma: ")
        
    ports = ports.split(",")
    
    for port in ports:
        
        port_number = int(port)
        
        if port_number < 0 or port_number > 65535:
            print("Port number must be between 0 and 65535")
            
        else:
            
            port_name = ""
            
            if port_number == 1023:
                port_name = "COM1"
            elif port_number == 1025:
                port_name = "COM2"
            elif port_number == 1026:
                port_name = "COM3"
            elif port_number == 1027:
                port_name = "COM4"
            elif port_number == 1028:
                port_name = "COM5"
            elif port_number == 1029:
                port_name = "COM6"
            elif port_number == 1030:
                port_name = "COM7"
            elif port_number == 1031:
                port_name = "COM8"
            elif port_number == 1032:
                port_name = "COM9"
            elif port_number == 1033:
                port_name = "COM10"
            elif port_number == 1034:
                port_name = "COM11"
            elif port_number == 1035:
                port_name = "COM12"
            elif port_number == 1036:
                port_name = "COM13"
            elif port_number == 1037:
                port_name = "COM14"
            elif port_number == 1038:
                port_name = "COM15"
            elif port_number == 1039:
                port_name = "COM16"
            elif port_number == 1040:
                port_name = "COM17"
            elif port_number == 1041:
                port_name = "COM18"
            elif port_number == 1042:
                port_name = "COM19"
            elif port_number == 1043:
                port_name = "COM20"
            elif port_number == 1044:
                port_name = "COM21"
            elif port_number == 1045:
                port_name = "COM22"
            elif port_number == 1046:
                port_name = "COM23"
            elif port_number == 1047:
                port_name = "COM24"
            elif port_number == 1048:
                port_name = "COM25"
            elif port_number == 1049:
                port_name = "COM26"
            elif port_number == 1050:
                port_name = "COM27"
            elif port_number == 1051:
                port_name = "COM28"
            elif port_number == 1052:
                port_name = "COM29"