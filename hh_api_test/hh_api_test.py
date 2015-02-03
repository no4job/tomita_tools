__author__ = 'mdu'
import requests
from furl import *
import sys
#test4
client_id="QG8LA1VUNJLROPLT7ERTKPPE5CDVAT8GBIC8O60CG7SHFVRL4P7BTT6S4QLJAQ5K"
client_secret="OP68TTUU3QG1P75S7D9GR4AG763T7UQI1LBP20D9IB7M2HREEJFGJ2589601DRFE"
#Step 1
ref_url="https://m.hh.ru/oauth/authorize?response_type=code&client_id={client_id}&state={state}&redirect_uri={redirect_uri}"
url=furl(ref_url).set(args={'response_type':'code','client_id':client_id})
print(url)
verify=False
r = requests.get(url,  verify=verify)
print(r.content)
sys.exit(0)
verify=False
#base_url="https://api.hh.ru/"
#command_url= "me"
scheme="https"
host="m.hh.ru"


command_url="oauth/authorize"
resource="oauth/authorize"

#access_token="I2FBHVENI01U2O2FNLORJPT5G4SF555BRVLB0V4KQMNLQN3TEP7H5P55479PG0BH"
headers={'User-Agent':'hhdata)', 'Host':'api.hh.ru','Accept':'*/*','Authorization':'Bearer '+ access_token}

r = requests.get(base_url+command_url, headers=headers, verify=verify )
print(r.content)

