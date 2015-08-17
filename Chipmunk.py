import re
from Crawler import Crawler
from Hoarder import Hoarder
from sets import Set

# put it all together
class Chipmunk:
    visited = Set([])
    def __init__(self, start, cutoff):
        self.start = start
        self.cutoff = cutoff
        self.crawler = Crawler()
        self.hoarder = Hoarder()

    def crawl(self):
        # go to link, crawl, download links as they come in.e
        # man, do we even need the tree? just hash the urls...
        counter = 0
        stack = [] # better in heap than on stack
        stack.append(start)
        while counter < cutoff && stack:
            cur = stack.pop()
            if cur not in visited:
                self.crawler.navigate(cur)
                visited.add(cur)
                links = findNextStrict(filterwebcomic)
                for l in links:
                    if l not in visited:
                        stack.append(l)
            counter++

    def findMainImage(self, driver):
        driver.find_elements_by_xpath('//*[@img]') # or something

    def filterwebcomic(self, cururl, links):
        # going left to right, are we a bigger number? add 0's if necessary
        regex = re.compile('[^0-9]')
        lo = float('inf')
        winner = None
        cur = regex.sub('', cururl)
        for link in links:
            next = regex.sub('', link)
            # normalize the magnitude
            cur = cur+ '0'*(len(next)-len(cur)) if len(next) > len(cur)
            next = next+ '0'*(len(cur)-len(next)) if len(cur) > len(next)
            # if it's increasing
            if next > cur:
                # and if it's minimal (can't just go with diff = 1, on account of chapters)
                if next-cur < lo:
                    winner = link
                    lo = next-cur
        return winner






