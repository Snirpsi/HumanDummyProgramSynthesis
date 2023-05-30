#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports. """    
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port > 0:
            
            subprocess.call(['sudo', 'ufwd', '-i', port])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 1])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 2])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 3])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 4])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 5])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 6])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 7])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 8])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 9])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 10])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 11])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 12])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 13])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 14])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 15])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 16])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 17])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 18])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 19])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 20])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 21])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 22])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 23])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 24])
            
            subprocess.call(['sudo', 'ufwd', '-i', port + 25