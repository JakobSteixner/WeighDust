#!/opt/local/bin/python
# On my MacBook, I'm using a MacPorts-installed Python for numerical calculations.
# If you have the relevant modules set up for use with your system's default Python,
# Replace with `/usr/bin/python`

import urllib2
import string, time
import pygrib

getfilename

class RequiredFile(pygrib.open):
    def __init__(self, repository, downloadfolders, idstring):
        self.repository = repository
        self.downloadfolders = downloadfolders
        success = -1
        while success:
            success = self._download_new()
            if success:
                time.sleep(1.5)
        self =pygrib.open(self.filelocation)
    def _download_new(self):
        #code to download speficied file, storing its location
        # as self.filelocation
        print ("downloading...")
        #code to test whether download was successful
        if True:
            return 0 #on success
        else:
            return -1
    
    def show_available(self):
        # return string object listing files that have previously
        # been successfully downloaded
        
        # uses self.downloadfolders
        return ""
        
    
    

