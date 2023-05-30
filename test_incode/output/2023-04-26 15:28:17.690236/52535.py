#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or adds words. """    
    
    # Open all ports
    ports = open('/proc/net/tcp').read().splitlines()
    
    # Add words to all ports
    for port in ports:
        words = port.split()
        for word in words:
            words = word.split(':')
            words[0] = words[0].replace('tcp', 'udp')
            words[1] = words[1].replace('tcp', 'udp')
            words[2] = words[2].replace('tcp', 'udp')
            words[3] = words[3].replace('tcp', 'udp')
            words[4] = words[4].replace('tcp', 'udp')
            words[5] = words[5].replace('tcp', 'udp')
            words[6] = words[6].replace('tcp', 'udp')
            words[7] = words[7].replace('tcp', 'udp')
            words[8] = words[8].replace('tcp', 'udp')
            words[9] = words[9].replace('tcp', 'udp')
            words[10] = words[10].replace('tcp', 'udp')
            words[11] = words[11].replace('tcp', 'udp')
            words[12] = words[12].replace('tcp', 'udp')
            words[13] = words[13].replace('tcp', 'udp')
            words[14] = words[14].replace('tcp', 'udp')
            words[15] = words[15].replace('tcp', 'udp')
            words[16] = words[16].replace('tcp', 'udp')
            words[17] = words[17].replace('tcp', 'udp')
            words[18] = words[18].replace('tcp', 'udp')
            words[19] = words[19].replace('tcp', 'udp')
            words[20] = words[20].replace('tcp', 'udp')
            words[21] = words[21].replace('tcp', 'udp')
            words[22] = words[22].replace('tcp', 'udp')
            words[23] = words[23].replace('tcp', 'udp')
            words[24] = words[24].replace('tcp', 'udp')
            words[25] = words[25].replace('tcp', 'udp')
            words[26] = words[26].replace('tcp', 'udp')
            words[27] = words[27].replace('tcp', 'udp')
            words[28] = words[28].replace('tcp', 'udp')
            words[29] = words[29].replace('tcp', 'udp