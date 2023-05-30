#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports and removes numbers. """    
    while True:
        ports = os.listdir('/dev/tty')
        for port in ports:
            if port.isdigit():
                os.system('sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT' % port)
        print('Done')
        time.sleep(1)
