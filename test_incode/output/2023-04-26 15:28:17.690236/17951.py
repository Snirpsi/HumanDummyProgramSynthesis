#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
        file = open(filename, 'r')
        
        lines = file.readlines()
        
        file.close()
        
        html = '<!DOCTYPE html><html><head><title>User Input</title></head><body>'
        
        for line in lines:
            html += line
            
        html += '</body></html>'
        
        sys.stdout.write(html)
        
    else:
        sys.stdout.write('Usage: python userinput.py <filename>\n')
        
