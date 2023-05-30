#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port. """    
    port = int(sys.argv[1])
    
    # Store the port in the database
    port = Port(port)
    port.save()
    
    # Print the port
    print(port)
    
    # Print the port in the database
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.objects.get(pk=port.pk))
    
    # Delete the port
    port.delete()
    
    # Print the port
    print(Port.