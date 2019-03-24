# OBS script to get shoutcast radio now playing (majority of internet radio stations)
# written by foxtrotdragon
#
# Need to shoutcast address for currentsong (usually an IP address)
# EX. "http://144.217.203.184:8398/currentsong?sid=1" Baka Radio
# easy way to find it is if there is a winamp link, or an windows media player link 
# EX. "https://144.217.203.184:8398/listen.pls" OR "mms://144.217.203.184:8398"
# remove the prefix and suffix if necessary so you just have the IP Address "144.217.203.184:8398"
# then you should find a now playing right click copy link and replace the URL
# you can change output.txt file name to whatever you desire
# you can change time.sleep(*) where * equals seconds to change loop speed, I do not reccomend doing less than 5 seconds for courtesy reasons 


import requests
import time
url = 'http://144.217.203.184:8398/currentsong?sid=1' #shoutcast current song, example used Bakaradio 
t = 'output.txt'			# declare "t" as desired output text named outtput.txt (create the document first with utf-8 encoding) if in a different folder put whole path IE: D:\Program Files\obs-studio\obs-plugins\output.txt

while True:
	r = requests.get(url)	# makes the url easy to work with NEEDS TO BE IN LOOP
	r.encoding	= 'utf-8' 	# force encoding utf-8 to prevent mojibake
	w = "Bakaradio: " + r.text # copies the text in url as "w" replace prefix with what you want if anything " add + "whatever you want it to say" if you want to add a suffix, Put a space between quotation and first letter for suffix"
	with open(t, 'r+', encoding = 'utf_8') as f:  # checks to see if the file is accurate
		found = False
		for line in f:
			if w in line:  						  # if text is accurate loop every 5 seconds
				found = True
		#print ("file is up to date")			  # for debug purposes to make sure it is updating properly
		time.sleep(5)
	
		if not found:							  # data is innacurate write over text file	
			with open(t, 'r+', encoding = 'utf_8') as f:
				f.seek(0)
				f.write(w)
			#print ("file has been updated")	  # for debug purposes to make sure it is updating properly
			time.sleep(1)
			
