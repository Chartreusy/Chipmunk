from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re
class Crawler:
    # class vars

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.curUrl = None

    def navigate(self, url):
        self.driver.get(url)
        self.curUrl = url

    def filterPage(self, method):
        method(self, driver)
    def findNext(self, regex):
       
        linkslist = [ e.get_attribute('outerHTML') for e in self.driver.find_elements_by_xpath("//*[@href]")]

        r = re.compile(regex)
        return filter(r.match, linkslist)

    # method just needs to give true/false from method(linkslist[i])

    def findNextStrict(self, method):
        linkslist = [ e.get_attribute('outerHTML') for e in self.driver.find_elements_by_xpath("//*[@href]")]
        return method(self.curUrl, linkslist)



    def download(self, regex):
        # apply filter to all links within page
        # download then send to hoarder for organization.
        a = 2


    def close(self):
        self.driver.close()



