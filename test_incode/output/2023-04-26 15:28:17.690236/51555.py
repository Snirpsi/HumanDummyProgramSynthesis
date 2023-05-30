#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove.py <list>")
        sys.exit()
    
    list1 = sys.argv[1]
    
    if len(list1) > 10:
        print("Error: list too long")
        sys.exit()
    
    list2 = []
    
    for x in list1:
        if x not in list2:
            list2.append(x)
    
    if len(list2) == 0:
        print("Error: list empty")
        sys.exit()
    
    list3 = []
    
    for x in list2:
        if x in list3:
            list3.remove(x)
        else:
            list3.append(x)
    
    if len(list3) == 0:
        print("Error: list empty")
        sys.exit()
    
    list4 = []
    
    for x in list3:
        list4.append(x*2)
    
    if len(list4) == 0:
        print("Error: list empty")
        sys.exit()
    
    print(list4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    