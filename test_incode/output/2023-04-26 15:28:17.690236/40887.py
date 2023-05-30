#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input or stores all ports. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    ports = ports.split(',')
    
    for port in ports:
        
        port = port.strip()
        
        if port == '':
            continue
        
        if port == 'all':
            
            ports = ports
            
        else:
            
            ports.append(port)
            
    ports = list(set(ports))
    
    if len(ports) == 0:
        print('No ports found')
        
    else:
        
        print('Ports found:')
        
        for port in ports:
            
            print('\t' + port)
            
        print('')
        
        print('Press any key to continue...')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        raw_input()
        
        print('')
        
        print('Done')
        
        print('')
        
        print('Press any key to exit')
        
        