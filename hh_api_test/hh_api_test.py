__author__ = 'mdu'
import requests
from furl import *
import sys
#test6
'''
Get information about proxy: request.py:getproxies_environment()
Windows proxy settings:
[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings]
"MigrateProxy"=dword:00000001
"ProxyEnable"=dword:00000001
"ProxyHttp1.1"=dword:00000000
"ProxyServer"="http://ProxyServername:80"
"ProxyOverride"="<local>

Ubuntu proxy settings
configuration file:cat /etc/environment(cat /etc/environment)->
http_proxy="http://127.0.0.1:8888/"
https_proxy="https://127.0.0.1:8888/"

system environment variables (printenv | grep -i proxy)->
NO_PROXY=localhost,127.0.0.0/8,::1
http_proxy=http://127.0.0.1:8888/
https_proxy=https://127.0.0.1:8888/
no_proxy=localhost,127.0.0.0/8,::1

reload changed variables from /etc/environment need logout->login or reboot

copy proxy SSL certificate file(PEM) to  /etc/ssl/certs/ca-certificates.crt/
sudo update-ca-certificates
'''
client_id="QG8LA1VUNJLROPLT7ERTKPPE5testCDVAT8GBIC8O60CG7SHFVRL4P7BTT6S4QLJAQ5K"
client_secret="OP68TTUU3QG1P75S7D9GR4AG763T7UQI1LBP20D9IB7M2HREEJFGJ2589601DRFE"
#Step 1
ref_url="https://m.hh.ru/oauth/authorize?response_type=code&client_id={client_id}&state={state}&redirect_uri={redirect_uri}"
url=furl(ref_url).set(args={'response_type':'code','client_id':client_id})
print(url)
#debug proxy - manual setting, for external debug proxy
use_debug_proxy = False
if use_debug_proxy:
    proxies = {'http' : 'http://192.168.1.2:8888',
           'https': 'http://192.168.1.2:8888'}
else:
    proxies = {}
#verify=True
verify=False
r = requests.get(url,  verify=verify , proxies=proxies)
print(r.content)
sys.exit(0)
verify=False
#verify=True
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

