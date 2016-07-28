__author__ = 'gpatarkatsishvili'

import xml.etree.ElementTree as etree
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import re



class JOBS:

    jobs_feed =[]

    def __init__(self):
        self.jobs_rss = urllib2.urlopen("http://jobs.ge/rss/")
        self.jobs_data = self.jobs_rss.read()

        #entire feed
        self.jobs_root = etree.fromstring(self.jobs_data)
        self.items = self.jobs_root.findall('channel/item')


    def get_vacancies(self, keywords = None):
        """
        get list of vacancies
        Parameters:
          keywords : string
                     using example : get_vacancies("პროგრამისტი_დეველოპერი") - it will returns applications which title contains words "პროგრამისტი" or "დეველოპერი"
        """

        #get title, description, link, pubdate from each application
        for entry in self.items:

            title = entry.findtext('title')
            #if search keyword doesn't exists - return all applications, if exists - search phrase in title and return only matches
            if keywords != None :
                search_phrases = keywords.replace("_","|")
                search_phrases_for_regex = '|'+search_phrases+'|'
                matches = re.search('/ '+search_phrases_for_regex+' /', title)
                #return keywords, title, matches
            else:
                matches = True

            if matches:
                link = entry.findtext('link')
                description = entry.findtext('description')
                pubDate = entry.findtext('pubDate')
                self.jobs_feed.append([title,link,description,pubDate])

        return self.jobs_feed