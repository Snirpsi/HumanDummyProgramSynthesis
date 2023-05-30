#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = 1
    
    numbers = []
    
    for i in range(number):
        numbers.append(i)
    
    numbers_str = ','.join(str(number) for number in numbers)
    
    print('Content-type: text/html')
    print('')
    print('<html><body>')
    print('<h1>Enumerate numbers</h1>')
    print('<hr>')
    print('<p style="font-size:16px">Numbers: %s' % numbers_str)
    print('<hr>')
    print('</body></html>')
    
