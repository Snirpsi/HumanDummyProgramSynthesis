#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers and opens all ports. """    
    while True:
        ports = open('/proc/net/tcp').read().splitlines()
        for port in ports:
            if port.find(':') != -1:
                ports.remove(port)
        for port in ports:
            subprocess.call(['iptables', '-D', 'INPUT', '-s', port, '-p', 'tcp', '--dport', str(port)])
            subprocess.call(['iptables', '-D', 'OUTPUT', '-s', port, '-p', 'tcp', '--dport', str(port)])
            subprocess.call(['iptables', '-D', 'FORWARD', '-s', port, '-p', 'tcp', '--dport', str(port)])
            subprocess.call(['iptables', '-D', 'PREROUTING', '-s', port, '-p', 'tcp', '--dport', str(port)])
        time.sleep(1)
</code>
<|/ a dscore=1 tags=python,linux,iptables,networking,network-programming |>
<| c |>
Thanks, this was very helpful!
<|/ c |>
<| a |>
I used the code from https://stackoverflow.com/a/9142907/1227829 and it works fine for me. 
<code>
import subprocess
import time

while True:
    ports = open('/proc/net/tcp').read().splitlines()
    for port in ports:
        if port.find(':') != -1:
            ports.remove(port)
    for port in ports:
        subprocess.call(['iptables', '-D', 'INPUT', '-s', port, '-p', 'tcp', '--dport', str(port)])
        subprocess.call(['iptables', '-D', 'OUTPUT', '-s', port, '-p', 'tcp', '--dport', str(port)])
        subprocess.call(['iptables', '-D', 'FORWARD', '-s', port, '-p', 'tcp', '--dport', str(port)])
        subprocess.call(['iptables', '-D', 'PREROUTING', '-s', port, '-p', 'tcp', '--dport', str(port)])
    time.sleep(1)
</code>
<|/ a dscore=0 tags=python,linux,iptables,networking,network-programming |>
<| c |>
Thanks, this was very helpful!
<|/ c |>
<| a |>
I used the code from https://stackoverflow.com/a/9142907/1227829 and it works fine for me. 
<code>
import subprocess
import time

while True:
    ports = open('/proc/net/tcp').read().splitlines()
    for port in ports:
        if port.find(':') != -1:
            ports.remove(port)
    for port in ports:
        subprocess.call(['iptables', '-D', 'INPUT', '-s', port, '-p', 'tcp', '--d