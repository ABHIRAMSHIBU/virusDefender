#!/usr/bin/python2
import os
if os.path.exists('/usr/bin/screen') and os.path.exists('/usr/bin/wget') :
	z=os.popen('ping -c 4 www.github.com').read()
	if '100% packet loss' in z or 'Name or service not known' in z :
		print "ERROR: Error communicating to server, update failed!"
	else :
		if os.path.exists("databases"):
			os.system("rm -rf databases")
		os.system("screen wget https://raw.githubusercontent.com/ABHIRAMSHIBU/virusDefender/master/updater/databases")
		if os.path.exists("databases"):
			print "Database update succeeded!"
		else:
			print "Database upgrade error occured 404."
else :
	print "ERROR : Executable not found","Try installing screen and wget"
