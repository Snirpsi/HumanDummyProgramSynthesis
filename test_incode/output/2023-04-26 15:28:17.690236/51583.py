#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers_str = ' '.join(numbers)
    
    numbers_str = numbers_str.replace(' ', '')
    
    numbers_str = numbers_str.replace(',', '')
    
    numbers_str = numbers_str.replace('-', '')
    
    numbers_str = numbers_str.replace('.', '')
    
    numbers_str = numbers_str.replace(';', '')
    
    numbers_str = numbers_str.replace(':', '')
    
    numbers_str = numbers_str.replace(';', '')
    
    numbers_str = numbers_str.replace('-', '')
    
    numbers_str = numbers_str.replace(' ', '')
    
    numbers_str = numbers_str.replace(',', '')
    
    numbers_str = numbers_str.replace('-', '')
    
    numbers_str = numbers_str.replace('.', '')
    
    numbers_str = numbers_str.replace(';', '')
    
    numbers_str = numbers_str.replace(':', '')
    
    numbers_str = numbers_str.replace('-', '')
    
    numbers_str = numbers_str.replace(' ', '')
    
    numbers_str = numbers_str.replace(',', '')
    
    numbers_str = numbers_str.replace('-', '')
    
    numbers_str = numbers_str.replace('.', '')
    
    numbers_str = numbers_str.replace(';', '')
    
    numbers_str = numbers_str.replace(':', '')
    
    numbers_str = numbers_str.replace('-', '')
    
    numbers_str = numbers_str.replace(' ', '')
    
    numbers_str = numbers_str.replace(',', '')
    
    numbers_str = numbers_str.replace('-', '')
    
    numbers_str = numbers_str.replace('.', '')
    
    numbers_str = numbers_str.replace(';', '')
    
    numbers_str = numbers_str.replace(':', '')
    
    numbers_str = numbers_str.replace('-', '')
    
    numbers_str = numbers_str.replace(' ', '')
    
    numbers_str = numbers_str.replace(',', '')
    
    numbers_str = numbers_str.replace('-', '')
    
    numbers_str = numbers_str.replace('.', '')
    
    numbers_str = numbers_str.replace(';', '')
    
    numbers_str = numbers_str.replace(':', '')
    
    numbers_str = numbers_str.replace('-', '')
