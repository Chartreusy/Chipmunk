import urllib

"""
This class has two functions. One is to keep track of everything we have
the second is to download things and to sort them into nice places, renaming them if necessary.
Need to maintain an external 
"""T
class Hoarder:

    # given a link, download the file
    def __init__(self):
        # need a location to dl them to
        # need a db of sorts to keep track fo what we already have
        a=2


    def locate(self, criterion):

    def getFile(self, url, dest):
        fileInfo = urllib.urlretrieve(url, dest)
        #print "%s - %s" % (fileInfo[0], fileInfo[1])