import socket
socket.setdefaulttimeout(2)
s=socket.socket()
s.connect(("192.168.1.132",9955))
print("C:input data (with 'end' for exit the program)")
goon=True
while(goon):
    print "C:-------------------------------------"
    print "C:Please input data:"
    indata=raw_input()
    s.send(indata+"\n") #must add "\n"
    data=s.recv(1024).strip('\n')
    if "end"!=data :
        print("C:receive result:"+data)
    else:
        goon=False;
        print("C:end...")
s.close()

