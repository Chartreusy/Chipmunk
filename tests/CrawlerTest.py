import platform 
import unittest
from selenium import webdriver



class CrawlerTest(unittest.TestCase):
    def setUp(self):
        self.crawler = Crawler()

    def testNavigateAndRetrieveLinks(self):
        crawler = self.crawler
        crawler.navigate("http://www.google.ca")
        ret =  crawler.findNext(".*")
        for r in ret:
            print r



    def tearDown(self):
        self.crawler.close()

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from Crawler import Crawler
    else:
        from Crawler import Crawler
    unittest.main()