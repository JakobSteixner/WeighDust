#!/opt/local/bin/python
# On my MacBook, I'm using a MacPorts-installed Python for numerical calculations.
# If you have the relevant modules set up for use with your system's default Python,
# Replace with `/usr/bin/python`

import urllib2
import string, time
import pygrib

getfilename

class RequiredFile(pygrib.open):
    """class to provide a pygrib.open instance for a data stream
    that may or may not be present locally. If present locally,
    a download is evaded, otherwise, the file is pulled from a specified
    repository.
    """
    def __init__(self, repository, downloadfolders, idstring, debugmode=False):
        self.repository = repository
        self.downloadfolders = downloadfolders
        success = -1
        while success:
            success = self._download_new()
            if success:
                time.sleep(2.5)
                # avoid accidental DoS
        self =pygrib.open(self.filelocation)
    def _download_new(self):
        #code to download speficied file, storing its location
        # as self.filelocation
        print ("downloading...")
        #code to test whether download was successful
        if True: #replace with check for successful download
            return 0 #on success
        else:
            return -1
    
    def show_available(self):
        # return string object listing files that have previously
        # been successfully downloaded
        
        # uses self.downloadfolders
        return ""
        
    
    

