__author__ = 'mdu'
import db_connect
import common_config
import data_source_config
import json
import requests
#from furl import *
#import furl
DEBUG_PROXY = False

def execute_request(request):
    if DEBUG_PROXY:
        proxies = {'http' : 'http://192.168.1.2:8888',
                   'https': 'http://192.168.1.2:8888'}
        verify=False
    else:
        proxies = {}
        verify=True

        r = requests.get(url,  verify=verify , proxies=proxies,headers=headers)
        print(r.content)