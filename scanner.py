#!/bin/python3
#usage: python3 scanner.py <ip>
#optional usage: if you would like to see each port getting checked, type a 'y' at the end
                    #-> example: python3 scanner.py <ip> y

import sys
import socket
from datetime import datetime

showProcess=False
openPorts = []
startPort=1
endPort=500

#Checking for the optional option for printing the process as we go through the ports
if len(sys.argv) == 3:
    arg2=sys.argv[2]
    if arg2.lower()=='y':
        showProcess=True
    target = socket.gethostbyname(sys.argv[1])
elif len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translating a hostname to IPv4
    #print(target)
else:
    print("Invalid amoung of arguments.")
    print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started "+str(datetime.now()))
print("-" * 50)


try:
        print(showProcess)
        for port in range(startPort,endPort):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #once again defining the socket
            socket.setdefaulttimeout(0.1) #Setting a timeout of 1 second for attempting to connect to a port
            result = s.connect_ex((target,port)) #returns an error indicator
            if (showProcess==True):
                print("Checking port {}".format(port)) #This is optional, it just shows what port is being scanned at the moment
            if result == 0: #If a 0 is returned, the port is open. If its a one, it is closed.
                print("Port {} is open".format(port))
                openPorts.append(port)
            s.close() #close the connection with the port

        #The following lines are printed at the end of the program runtime
        print("Scan finished "+str(datetime.now()))
        print("The following ports have been found to be open within the range " +str(startPort) +"-"+str(endPort)+":")
        print(openPorts)
#If user decides to stop execution by means of keyboard interrupt (Ctrl+c)
except KeyboardInterrupt:
        print("\nExiting program")
        sys.exit()

#If DNS does not resolve to anything
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

#Port connection error
except socket.error:
    print("Could not connect to server")
    sys.exit()
