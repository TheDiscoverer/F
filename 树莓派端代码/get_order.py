import socket
#socket.setdefaulttimeout(2)
s=socket.socket()
s.connect(("192.168.1.132",9955))
goon=True
while(goon):
    print "wait";
    data=s.recv(1024).strip('\n')
    while(data!=''):
        print data
        data=s.recv(1024).strip('\n')
s.close()

