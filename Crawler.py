from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re
class Crawler:
    # class vars

    def __init__(self):
        # instance vars
        #firefox_bin = FirefoxBinary("/cygdrive/c/Program Files (x86)/Mozilla Firefox/firefox.exe")
        #self.driver = webdriver.Firefox(firefox_binary=firefox_bin)
        self.driver = webdriver.Chrome()

    def navigate(self, url):
        self.driver.get(url)

    def findNext(self, regex):
        driver = self.driver
        # apply filter to all links within current page
        # regex for now, probably a method later on.
        # add them to list
        linkslist = [ e.get_attribute('outerHTML') for e in driver.find_elements_by_xpath("//*[@href]")]

        r = re.compile(regex)
        return filter(r.match, linkslist)



    def download(self, regex):
        # apply filter to all links within page
        # download then send to hoarder for organization.
        a = 2


    def close(self):
        self.driver.close()



