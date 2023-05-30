#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and converts all ports. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    ports.sort()
    
    ports_str = ','.join(str(p) for p in ports)
    
    print('''
<html>
<head>
<title>Port Converter</title>
</head>
<body>
<h1>Port Converter</h1>
<p>Port Converter is a simple web server that converts all ports.</p>
<p>Ports: %s</p>
</body>
</html>
''' % ports_str)
    
