import socket 
import sys

Client = socket.socket()
host = '192.168.0.162'
port = 4848

try:
    Client.connect((host,port))
    print ('connected! ')
except socket.error as e:
    print ( str(e) )

loop = True

while loop:
    print ('\n \n python calculator ')
    print (' 1. logarithmic expression ')
    print (' 2. square root expression ')
    print (' 3. exponential expression ')
    print (' 4. exit ')

    ans = input ('\n enter number of choice: ' )
    Client.send(ans.encode())

    if ans == '1':
        print ('\n [logarithmic] ')
        numb = input ('\n enter number: ')
        Client.send(numb.encode())
        tot = Client.recv(1024)

        print ( '\n answer ( '+ numb +' ) : ' + str(tot.decode()))
    elif ans == '2':
        root = True
        while root:
            print ('\n [square root] ')
            numb = input ('\n enter number: ')
            if int(numb) > -1 :
                root = False
                Client.send(numb.encode())
                tot = Client.recv(1024)
            else:
                print ('\n negative number is not allowed for square root! ')

        print ( '\n answer ( ' + numb +' ): ' + str(tot.decode()))


    elif ans == '3':
        print ('\n [exponential]')
        numb = input ('\n enter number: ')
        Client.send(numb.encode())
        tot = Client.recv(1024)

        print ( '\n answer ( ' + numb + ' ): ' + str(tot.decode()))


    elif ans == '4':
        Client.close()
        sys.exit()
    else:
        print ('\n input is invalid. please try again')

    input ( '\n please press enter to proceed')
