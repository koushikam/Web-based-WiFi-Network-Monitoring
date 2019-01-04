# Web-based-WiFi-Network-Monitoring
Monitoring Signal strength of near by Wifi Hotspots update results every 30 seconds


a) write Python function that run the following shell command

      Windows OS: netsh wlan show all (Windows OS) or Linux OS:  iwconfig to find name of your WLAN interface and then use iwlist command to list all APs

   Function parses the command output and return an array of JSON objects with following properties ssid, bssid, signal level, primary channel

b) Configure an Apache HTTP Server that can run CGI Python scripts
 For installing Apache on Ubuntu you need only one command (sudo apt-get install apache2), but to support cgi you need to modify settings. Look at this website https://code-maven.com/set-up-cgi-with-apache 

c) Write CGI file that

1. call the function given in a),

 2. orders the returned array by channel index,

 3. calculates level of contention for 2.4GHz band for each channel index as contention_level=sum((1-abs(channel_i-index)/5)*signal_level_i)

4.displays the bssid,ssid and channel of each AP and plot graphs of contention level for 2.4GHz band

5. refreshes page every 30 seconds
