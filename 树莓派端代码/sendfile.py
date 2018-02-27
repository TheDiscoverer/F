import time
import threading
import socket
import os
 
class Client():
    def __init__(self):
        address = ('192.168.1.132', 8086)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
	fn=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'.png'
       # fn='5.png'
	str='raspistill -o '+fn+' -rot 180'
	os.system(str)
        ff = os.path.normcase(fn)
        try:
            f = open(fn, 'rb')
            sendFile = SendFile(s,f)
            sendFile.start()
            print 'start to send file.'
        except IOError:
            print 'open err'
 
 
class SendFile(threading.Thread):
    def __init__(self, sock, file):
        threading.Thread.__init__(self)
        self.file = file
        self.sock = sock
 
    def run(self):
        print self.file
        BUFSIZE = 1024
        count = 0
        name = self.file.name+'\r'
        #for i in range(1, BUFSIZE - len(self.file.filename) -1):
        #name += '?'
        #print name
        self.sock.send(self.file.name+"\n")
        while True:
            print BUFSIZE
            fdata = self.file.read(BUFSIZE)
            if not fdata:
                print 'no data.'
                break
            self.sock.send(fdata)
            count += 1
            if len(fdata) != BUFSIZE:
                print 'count:'+str(count)
                print len(fdata)
            nRead = len(fdata)
 
        print 'send file finished.'
        self.file.close()
        self.sock.close()
        print 'close socket'
 
c = Client()

