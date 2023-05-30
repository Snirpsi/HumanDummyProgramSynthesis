#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    import math
    import random
    import socket
    
    HOST, PORT = 'localhost', 8000
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print('Got connection from', addr)
        
        conn.send('HTTP/1.1 200 OK\r\n')
        conn.send('Content-Type: text/html\r\n')
        conn.send('\r\n')
        
        conn.send('<html><body><h1>Multiplication</h1>')
        conn.send('<p>')
        
        conn.send('<table>')
        
        conn.send('<tr>')
        conn.send('<td>')
        conn.send('Enter the numbers to be multiplied:')
        conn.send('</td>')
        conn.send('<td>')
        
        numbers = []
        
        while True:
            number = input('Enter a number: ')
            numbers.append(number)
            
            if len(numbers) == 2:
                break
        
        numbers = list(map(int, numbers))
        
        conn.send('<td>')
        conn.send('The result is')
        conn.send('</td>')
        conn.send('<td>')
        
        conn.send('')
        
        for number in numbers:
            conn.send('')
            
            conn.send('<tr>')
            conn.send('<td>')
            conn.send('%g' % number)
            conn.send('</td>')
            conn.send('<td>')
            
            conn.send('%g' % number * number)
            conn.send('</td>')
            conn.send('<td>')
            
            conn.send('%g' % number * number * number)
            conn.send('</td>')
            
            conn.send('</tr>')
            
        conn.send('</table>')
        
        conn.send('</body></html>')
        
        conn.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        