#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and converts words. """    
    ports = openports()
    words = []
    for port in ports:
        words.append(port.read())
    words = [word.upper() for word in words]
    words = [word for word in words if word != '']
    words = [word for word in words if word != ' ']
    words = [word for word in words if word != '\n']
    words = [word for word in words if word != '\r']
    words = [word for word in words if word != '\t']
    words = [word for word in words if word != '\t\n']
    words = [word for word in words if word != '\t\r']
    words = [word for word in words if word != '\t\n\r']
    words = [word for word in words if word != '\t\n\r\t']
    words = [word for word in words if word != '\t\n\r\t\n']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r\t\n\r']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r\t\n\r\t\r\t']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r\t\n\r\t\r\t\r\t']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r\t\n\r\t\r\t\r\t\r\t']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r\t\n\r\t\r\t\r\t\r\t\r\t']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r\t\n\r\t\r\t\r\t\r\t\r\t\r\t']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r\t\n\r\t\r\t\r\t\r\t\r\t\r\t']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r\t\n\r\t\r\t\r\t\r\t\r\t\r\t\r\t']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r\t\n\r\t\r\t\r\t\r\t\r\t\r\t\r\t']
    words = [word for word in words if word != '\t\n\r\t\n\r\t\r\t\n\r\t\r\t\r\t\r\t\r\t\r\t\r\t']
    words = [