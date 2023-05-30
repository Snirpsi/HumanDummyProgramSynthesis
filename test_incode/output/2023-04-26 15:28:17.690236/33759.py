#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and enumerates a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    numbers = [int(number) for number in sys.argv[2:]]
    
    ports.sort()
    numbers.sort()
    
    ports_str = ','.join(str(port) for port in ports)
    numbers_str = ','.join(str(number) for number in numbers)
    
    ports_str = ports_str.replace(',','')
    numbers_str = numbers_str.replace(',','')
    
    ports_str = ports_str.replace(' ','')
    numbers_str = numbers_str.replace(' ','')
    
    ports_str = ports_str.replace('-','')
    numbers_str = numbers_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    numbers_str = numbers_str.replace('.','')
    
    ports_str = ports_str.replace(',','')
    numbers_str = numbers_str.replace(',','')
    
    ports_str = ports_str.replace(':','')
    numbers_str = numbers_str.replace(':','')
    
    ports_str = ports_str.replace(';','')
    numbers_str = numbers_str.replace(';','')
    
    ports_str = ports_str.replace(' ','')
    numbers_str = numbers_str.replace(' ','')
    
    ports_str = ports_str.replace('-','')
    numbers_str = numbers_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    numbers_str = numbers_str.replace('.','')
    
    ports_str = ports_str.replace(',','')
    numbers_str = numbers_str.replace(',','')
    
    ports_str = ports_str.replace(':','')
    numbers_str = numbers_str.replace(':','')
    
    ports_str = ports_str.replace(';','')
    numbers_str = numbers_str.replace(';','')
    
    ports_str = ports_str.replace(' ','')
    numbers_str = numbers_str.replace(' ','')
    
    ports_str = ports_str.replace('-','')
    numbers_str = numbers_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    numbers_str = numbers_str.replace('.','')
    
    ports_str = ports_str.replace(',','')
    numbers_str = numbers_str.replace(',','')
    
    ports_str = port