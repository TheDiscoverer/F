import time
import threading
import socket
import os

class Client():
    def __init__(self):
        fn=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'.png'
        address = ('192.168.2.102', 9960)
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect(address)
        str='raspistill -o '+fn+' -rot 90 -t 1000 -w 1024 -h 768'
        os.system(str)
        ff = os.path.normcase(fn)
        try:
            f = open(fn, 'rb')
            sendFile = SendFile(sock,f)
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
        #
        self.sock.send(self.file.name+"\n")
        print "uploading..."
	while True:
           # print BUFSIZE
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
	os.system("rm "+self.file.name)
        self.file.close()
	self.sock.close()


