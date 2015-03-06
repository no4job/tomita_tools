__author__ = 'mdu'
from tools import *
import re
import configparser

#Tool settings
PATH = "K:\\all"
CFG_FILE = "K:\\search\\search_patterns.cfg"
config = configparser.ConfigParser()
config.read(CFG_FILE)
file_pattern_id=config['DEFAULT']['file_pattern_id']
file_pattern_type=config['DEFAULT']['file_pattern_type']

# check recursively for non printable characters
files=[]
dir_name_counter = 0
f_name_counter = 0
f_name_matched_counter = 0
print("Start file selection")
# traverse all dirs and files recursively
for dir in os.walk(top=PATH):
    # test and rename file names
    for f_name in dir[2]:
        m_type=re.match(file_pattern_type, f_name, re.IGNORECASE)
        m_id=re.match(file_pattern_id, f_name, re.IGNORECASE)
        if  m_type and m_id:
            #print ("f:",m_id.group("id"),":", os.path.join(dir[0],f_name))
            files.append([m_id.group("id"),dir[0],f_name])
            f_name_matched_counter+=1
        elif  m_type and not m_id :
            f_name_counter+=1
        else:
            f_name_counter+=1
print("End file selection")
print ("file names:",f_name_counter )
print ("matched file names:",f_name_matched_counter )
# search duplicated id
print("Start search id duplicates")
files_duplicated=dict()
for f in files:
    if f[0] in files_duplicated:
        files_duplicated[f[0]]+=[files.index(f)]
    else:
        files_duplicated[f[0]]=[files.index(f)]
#for i in [[index for index in files_duplicated[id]] for id  in files_duplicated if len(files_duplicated[id])>1 ]:
f_name_duplicated=0
total_duplicated_f_size=0
# print duplicated id
for id  in sorted([id for id in files_duplicated if len(files_duplicated[id])>1], key= lambda id:int(id),reverse=True):
    print ("*"*60)
    for index  in files_duplicated[id]:
        full_f_name=os.path.join(files[index][1],files[index][2])
        f_size=os.path.getsize(full_f_name)
        total_duplicated_f_size+=f_size
        f_name_duplicated+=1
        print (files[index][0],":",f_size//1000000,"MB:",full_f_name)

print("End search id duplicates")
print("Files with id duplicates:",f_name_duplicated)
print("Total size of files with duplicated id:",total_duplicated_f_size//1000000,"MB")
exit(0)


