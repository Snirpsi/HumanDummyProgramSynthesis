#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or opens a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    words = []
    
    if port == 4242:
        words.append('http')
    elif port == 4243:
        words.append('https')
    elif port == 4244:
        words.append('ftp')
    elif port == 4245:
        words.append('ftps')
    elif port == 4246:
        words.append('gopher')
    elif port == 4247:
        words.append('gophers')
    elif port == 4248:
        words.append('ldap')
    elif port == 4249:
        words.append('ldaps')
    elif port == 4250:
        words.append('mailto')
    elif port == 4251:
        words.append('news')
    elif port == 4252:
        words.append('nntp')
    elif port == 4253:
        words.append('nntps')
    elif port == 4254:
        words.append('telnet')
    elif port == 4255:
        words.append('telnets')
    elif port == 4256:
        words.append('imap')
    elif port == 4257:
        words.append('imaps')
    elif port == 4258:
        words.append('pop3')
    elif port == 4259:
        words.append('pop3')
    elif port == 4261:
        words.append('pop3')
    elif port == 4262:
        words.append('pop3')
    elif port == 4263:
        words.append('pop3')
    elif port == 4264:
        words.append('pop3')
    elif port == 4270:
        words.append('pop3')
    elif port == 4271:
        words.append('pop3')
    elif port == 4272:
        words.append('pop3')
    elif port == 4273:
        words.append('pop3')
    elif port == 4274:
        words.append('pop3')
    elif port == 4275:
        words.append('pop3')
    elif port == 4276:
        words.append('pop3')
    elif port == 4277:
        words.append('pop3')
    elif port == 4278:
        words.append('pop3')
    elif port == 4279:
        words.append('pop3')
    elif port == 4280:
        words.append('pop3')
    elif port == 4281:
        words.append('pop3')
    elif port == 4282:
        words.append('pop3')
    elif port == 4283:
