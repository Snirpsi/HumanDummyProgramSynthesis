#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or multiplyes a port. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    words = []
    
    for i in range(0, 10):
        words.append(str(i))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 1))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 2))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 3))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 4))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 5))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 6))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 7))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 8))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 9))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 10))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 11))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 12))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 13))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 14))
    
    print("\n".join(words))
    
    print("*" * 80)
    
    for i in range(0, 10):
        words.append(str(i * port + 15))
    
    print("\n".join(word