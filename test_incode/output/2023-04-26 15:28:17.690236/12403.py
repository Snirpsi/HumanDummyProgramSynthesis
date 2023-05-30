#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and adds all ports. """    
    
    ports = open('/etc/openvswitch/conf.d/ovs-vswitchd.conf').read().splitlines()
    
    ports += [':'.join(['%d' % (i+1) for i in range(1024)]) for x in range(1024)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65535)]) for x in range(65535)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65536)]) for x in range(65536)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65537)]) for x in range(65537)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65538)]) for x in range(65538)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65539)]) for x in range(65539)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65540)]) for x in range(65540)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65541)]) for x in range(65541)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65542)]) for x in range(65542)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65543)]) for x in range(65543)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65544)]) for x in range(65544)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65545)]) for x in range(65545)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65546)]) for x in range(65546)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65547)]) for x in range(65547)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65548)]) for x in range(65548)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65549)]) for x in range(65549)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65550)]) for x in range(65550)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65551)]) for x in range(65551)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65552)]) for x in range(65552)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65553)]) for x in range(65553)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65554)]) for x in range(65554)]
    
    ports += [':'.join(['%d' % (i+1) for i in range(65555)]) for 