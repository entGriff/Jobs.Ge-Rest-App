# Jobs.Ge Rest App 
Jobs.ge is one of the most popular site in Georgia, where you can find a lot of vacancies in Georgia. 

Using this app you can get list of all vacancies from jobs.ge in json format, you can also search through job title and get detail description of each vacancy.

### Installation
You just need pip for install this package
```sh
$ pip install jobsge
```

### How to use  package in Django
First you need add something like this in  your "urls.py" file : 
```python
urlpatterns = [
    url(r'^get_jobs/$', get_jobs),
    url(r'^get_jobs/(?P<keywords>\w+)', get_jobs),
    url(r'^get_concrete_job/(?P<id>\w+)', get_concrete_jobs),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

After this, You Can create methods in your Controller "views.py"


```python
from django.http import Http404, HttpResponse
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
from jobsge.concrete_jobs import CONCRETE_JOBS
from jobsge.jobs import JOBS

def get_jobs(request, keywords=None):
    jobs = JOBS()
    return HttpResponse(json.dumps(jobs.get_vacancies(keywords)),  content_type="application/json")

def get_concrete_jobs(request, id):
    ## instance method
    # concrete_jobs = CONCRETE_JOBS(id)
    # job_info = concrete_jobs.get_concrete()
    # return  HttpResponse(json.dumps({"jobs_info": job_info}))

    ## static method
    return  HttpResponse(json.dumps({"job_info": CONCRETE_JOBS.get_job_info(id)}))
```

It's all, now everything is ready to run and test it in browser : 

#### All vacancies: 
![get_jobs](https://cloud.githubusercontent.com/assets/2203893/17248440/9b5bfc32-55ab-11e6-84a1-a77e420bc618.PNG)

#### Search vacancies, who has "დეველოპერი" or   "არქიტექტორი"  in title  
![get_jobs_find](https://cloud.githubusercontent.com/assets/2203893/17248441/9b5ea716-55ab-11e6-8b22-ed3866ca464e.PNG)

#### Get description of concrete job:

![get_concrete_job](https://cloud.githubusercontent.com/assets/2203893/17248439/9b58a334-55ab-11e6-9bd9-ef88d155168f.PNG)




