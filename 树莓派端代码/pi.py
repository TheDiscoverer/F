import socket
import os
from weightValue import *
from getWeight import *
from getPicture import *
from getDistance import *
from uptem import *
class pai(threading.Thread):
	def run(self):
		Client()
class pi(threading.Thread):
	def run(self):
		dis=checkdist()
		while dis>0.1:
			print dis,"m"
			time.sleep(1)
			dis=checkdist()
		u=pai()
		u.start()

class upload(threading.Thread):
	def run(self):
		while(True):
			while(getTem()==0):
				time.sleep(0.3)
			time.sleep(60*5)	

class upIntake(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.weight1=getweightValue();
	def run(self):
		print "2333"
		time.sleep(100)
		weight2=getweightValue()
	        data = {'weight1':self.weight1,'weight2':weight2}
       		requrl = "http://192.168.2.102/test/sendweight12.php"
       		data_urlencode = urllib.urlencode(data)
        	req = urllib2.Request(url = requrl,data =data_urlencode)
      		res_data = urllib2.urlopen(req)

up =upload()
up.start()
s=socket.socket()
s.connect(("192.168.2.102",9955))
goon=True
if(goon):
    print "wait";
    data=s.recv(1024).strip('\n')
    while(data!=''):
        data=data[:-1]
	print data
        if cmp(data,"getWeight")==0:
		print weight()
       	if cmp(data,"getPicture")==0:
		print Client()
	if cmp(data[0:5],"zhuan")==0:
		v=int(data[6:]);
		print "ss", v
		getweightValue()
		while(getweightValue()<v):
			os.system("python zhuan.py 360 1")
		print getweightValue()
		up=upIntake()
		up.start()
		p=pi()
		p.start()
	data=s.recv(1024).strip('\n')
s.close()
