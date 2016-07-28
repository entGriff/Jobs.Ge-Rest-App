__author__ = 'gpatarkatsishvili'

from bs4 import BeautifulSoup
import requests


class CONCRETE_JOBS:

    _job_headline =[]
    _job_info = {}

    def __init__(self, url):
        self.url = "http://jobs.ge/" + url +"/"
        self.jobsGe_request  = requests.get(self.url)
        self.soup = BeautifulSoup(self.jobsGe_request.text)

    def get_concrete(self):
        #get headline info of concrete job
        self._job_info = self.get__job_headline()

        #get description of concrete job
        self._job_info['აღწერილობა'] = self.get_job_description()

        return self._job_info

    def get__job_headline(self):
        for headline in  self.soup.find_all('td', {'class':"adtitle"}):
            self._job_headline.append(headline.get_text())
        #convert list as string, split text as key-value and  next convert as dictionary
        _job_headline_as_string = ','.join(self._job_headline).replace("/", ",")
        return  dict(x.strip().split(':') for x in _job_headline_as_string.split(','))

    def get_job_description(self):
         return self.soup.find_all('table', {'class':"ad"})[-1].get_text()


    @staticmethod
    def get__job_info(id):
        concrete_job = CONCRETE_JOBS(id)
        return concrete_job.get_concrete()