#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words and converts numbers. """    
    
    words = []
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = line.split(' ')
        
        for word in words:
            word = word.strip()
            
            if word == '':
                continue
            
            number = word[-1]
            
            if number == '0':
                number = '1'
            
            numbers.append(number)
            
    numbers = ''.join(numbers)
    
    words = numbers.split(' ')
    
    for word in words:
        word = word.strip()
        
        if word == '':
            continue
        
        word = word.replace(' ', '')
        
        if word == '':
            continue
        
        word = word.replace(',', '')
        
        if word == '':
            continue
        
        word = word.replace('.', '')
        
        if word == '':
            continue
        
        word = word.replace('-', '')
        
        if word == '':
            continue
        
        word = word.replace(' ', '')
        
        if word == '':
            continue
        
        word = word.replace(':', '')
        
        if word == '':
            continue
        
        word = word.replace(';', '')
        
        if word == '':
            continue
        
        word = word.replace('?', '')
        
        if word == '':
            continue
        
        word = word.replace('!', '')
        
        if word == '':
            continue
        
        word = word.replace('\'', '')
        
        if word == '':
            continue
        
        word = word.replace('(', '')
        
        if word == '':
            continue
        
        word = word.replace(')', '')
        
        if word == '':
            continue
        
        word = word.replace(',', '')
        
        if word == '':
            continue
        
        word = word.replace('.', '')
        
        if word == '':
            continue
        
        word = word.replace('-', '')
        
        if word == '':
            continue
        
        word = word.replace(' ', '')
        
        if word == '':
            continue
        
        word = word.replace(':', '')
        
        if word == '':
            continue
        
        word = word.replace(';', '')
        
        if word == '':
            continue
        
        word = word.replace('?', '')
        
        if word == '':
            continue
        
        word = word.replace('!', '')
        
        if word == '':
            continue
        
        word = word.replace('\'', '')
        
        if word == '':
            continue
        
        word = word.replace('(', '')
        
        if word == '