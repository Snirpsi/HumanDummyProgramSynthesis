#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of numbers or iterates over all ports. """    
    ports = [
        port for port in os.listdir('/sys/bus/usb/devices/') 
        if os.path.isdir('/sys/bus/usb/devices/' + port) 
        and 'usb' in os.listdir('/sys/bus/usb/devices/' + port) 
        and '0' in os.listdir('/sys/bus/usb/devices/' + port + '/