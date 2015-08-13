import os
import unittest
class HoarderTest(unittest.TestCase):
    def setUp(self):
        self.hoarder = Hoarder()
    def testdownload(self):
       self.hoarder.getFile("https://40.media.tumblr.com/58d97fe8e72a0e9ead5a29fc7d636f51/tumblr_mnbdg6nrPV1s0onzzo1_540.jpg",
                            "testhoarder.jpg")
       assert os.path.isfile("testhoarder.jpg")

    def tearDown(self):
        os.remove("testhoarder.jpg")


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from Hoarder import Hoarder
    else:
        from Hoarder import Hoarder
    unittest.main()