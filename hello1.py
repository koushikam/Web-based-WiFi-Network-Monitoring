#!/usr/bin/python
#__init__.py
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word! This is my first CGI program</h2>'
print '<META HTTP-EQUIV="refresh" CONTENT="30">'

import os,sys
import cgi
import cgitb; cgitb.enable()
import matplotlib
import cStringIO
# set HOME environment variable to a directory the httpd server can write to
os.environ[ 'HOME' ] = '/tmp/'

# chose a non-GUI backend
matplotlib.use( 'Agg' )

#Deals with inputing data into python from the html form
form = cgi.FieldStorage()
#sys.path.insert(0, '/usr/lib/cgi-bin/')
sys.path.append(os.path.join(os.path.dirname('/usr/lib/cgi-bin/'), '..'))



import matplotlib.pyplot as plt
import numpy as np
import subprocess as s
import json
import re
from iwlist import wifi_scan
import matplotlib.pyplot as plt
#!/usr/bin/env python
  

def doit():
    My_wifi = s.check_output(["iwconfig"])
    print My_wifi

    APs_Json,len_AP = wifi_scan()
    APs = json.loads(APs_Json) # coverting it back to Python Object
    AP_d=[]
    format = "png"
    sio = cStringIO.StringIO()
    for i in range(len_AP):
        if APs[i]["Freq"]<3:
            AP_d = np.append(AP_d,APs[i])

    CI=[]; # Calculate contention index        
    if len(AP_d)>0:
        #print AP_d
        CI= np.array([ np.sum([(1-np.abs(AP_d[i]["Primary Channel"]-(index+1))/5)*(10**((AP_d[i]["Power[dBm]"]-30)/10)) for i in range(len(AP_d))]) for index in np.arange(11)])   #contention_level=sum((1-abs(channel_i-index)/5)*signal_level_i)
        plt.plot(np.arange(11)+1,CI,linewidth=2)
	plt.ylabel('Channel contention')
	plt.xlabel('Channel Index')
	plt.title('Channel Contetion Level Graph')
	plt.grid()
        #contention_level=sum((1-abs(channel_i-index)/5)*signal_level_i)
        plt.savefig(sio, format=format)

        data_uri = sio.getvalue().encode('base64').replace('\n', '')
        img_tag = '<img src="data:image/png;base64,{0}" alt="sucka" />'.format(data_uri)

        print("Content-type: text/html\n")
        print("<title>Try Ageen</title>")
        print("<h1>Access Point Contention Plot</h1>")
        print(img_tag)
	print("<h1>=================================== AP details ================================</h1>")
	print("<h1> Channel INFO:</h1>")
	for i in range(len(AP_d)):
		print "SSID: %s\t 'BSSID:'%s\t 'Channel:'%f \t  <br/>" % (AP_d[i]["SSID"], AP_d[i]["BSSID/MAC"],AP_d[i]["Primary Channel"])
		#print 'SSID:',AP_d[i]["SSID"],'BSSID:',AP_d[i]["BSSID/MAC"],'Channel:', AP_d[i]["Primary Channel"]
		
	print '=============================== APs Details =================================='
    
    else:
	#print '\n =================================== Message ================================'
	print("<h1>=================================== Message ================================</h1>")
        print ("<h1>Sorry!!!!!!!!! No 2.4GHz wifi were scanned</h1>")
	#print("<h1>=================================== Message ================================</h1>")
    
 
    

doit()
os.getcwd()
print '</body>'
print '</html>'


