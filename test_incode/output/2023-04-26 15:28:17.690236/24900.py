#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        content = f.read()
        
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content.replace('[', '{{')
    content = content.replace(']', '}}')
    
    content = content.replace('{{', '[')
    content = content.replace('}}', ']')
    
    content = content