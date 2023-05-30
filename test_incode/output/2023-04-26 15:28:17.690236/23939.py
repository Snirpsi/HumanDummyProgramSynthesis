#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and removes all ports. """    
    ports = input("Enter the ports to remove: ")
    ports = ports.split(",")
    for port in ports:
        if port not in ports:
            print("Port %s is not in list" % port)
        else:
            ports.remove(port)
    print(ports)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for the answer. I am new to python and have never used the csv module. Can you please explain the code a little bit?
<|/ c |>
<| c |>
I added some comments to the code. Hope it helps.
<|/ c |>
<| c |>
Thank you for the help. I understand what you are doing now. I am still getting an error when I try to run this code. 
Traceback (most recent call last):
  File "C:\Users\user\Desktop\PortList.py", line 5, in <module>
    ports = input("Enter the ports to remove: ")
TypeError: input expected at most 1 arguments, got 2
<|/ c |>
<| c |>
I added some comments to the code. Hope it helps.
<|/ c |>
<| c |>
Thank you for the help. I understand what you are doing now. I am still getting an error when I try to run this code. 
Traceback (most recent call last):
  File "C:\Users\user\Desktop\PortList.py", line 5, in <module>
    ports = input("Enter the ports to remove: ")
TypeError: input expected at most 1 arguments, got 2
<|/ c |>
<| a tags=python,python-3.x |>
<code>
import csv
with open('ports.csv') as csvfile:
    ports = csv.reader(csvfile)
    for row in ports:
        if row[0] not in ports:
            print("Port %s is not in list" % row[0])
        else:
            ports.remove(row[0])
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for the answer. I am new to python and have never used the csv module. Can you please explain the code a little bit?
<|/ c |>
<| c |>
I added some comments to the code. Hope it helps.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
import csv
with open('ports.csv') as csvfile:
    ports = csv.reader(csvfile)
    for row in ports:
        if row[0] not in ports:
            print("Port %s is not in list" % row[0])
        else:
            ports.remove(row[0])
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for the answer. I am new to python and have never used the csv module. Can you please explain the code a little 