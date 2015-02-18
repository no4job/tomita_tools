__author__ = 'mdu'
import os
import sys
import codecs
#import tools
from tools import *
from glob import glob
from unidecode import unidecode
#x=u'\xe0'.encode("utf-8", errors='replace').decode("utf-8", errors='replace' )
x=u'\xe0'
print (sys.stdout.encoding)
#sys.setdefaultencoding(sys.stdout.encoding or sys.stderr.encoding)
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout,'replace')
#print ('\xe9')
print ('шншшнншнр')
print (x.encode('cp1251','replace').decode('cp1251'))
#exit(0)

#PATH = "K:\\all".encode("cp1251").decode("cp1251")
PATH = "K:\\all"
#print(os.path.join(PATH, '*'))
#print (sys.getfilesystemencoding())
#result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*'))]
#result = [y for y in os.walk(PATH.encode(encoding='MBCS'))]
#for x in os.walk(PATH.encode(encoding='MBCS')):
#    print ("x=",x)
OUTPUT_ENCODING='cp1251'
files=[]
#dirs = [x for x in os.walk(PATH.encode(encoding='MBCS')) ]
dirs = [x for x in os.walk(PATH) ]
#print (dirs)
non_printable_dir_name_counter = 0
non_printable_f_name_counter = 0
for dir in dirs:
    non_printable_positions=non_printable(dir[0],OUTPUT_ENCODING)
    if (non_printable_positions):
        print ("d:",non_printable_positions, dir[0].replace('\\\\', '\\').encode('cp1251','replace').decode('cp1251'),
               unidecode(dir[0].replace('\\\\', '\\')))
        non_printable_dir_name_counter+=1
    for f_name in dir[2]:
        #f_set= [dir[0].decode(encoding='MBCS'),f_name,'']
        f_set= [dir[0],f_name,'']
        files.append(f_set)
        non_printable_positions=non_printable(f_name,OUTPUT_ENCODING)
        if (non_printable_positions):
            print ("f:",non_printable_positions, dir[0].replace('\\\\', '\\').encode('cp1251','replace').decode('cp1251'),
             " : ",f_name.replace('\\\\', '\\').encode('cp1251','replace').decode('cp1251'),
             unidecode(f_name.replace('\\\\', '\\')))
            non_printable_f_name_counter+=1

#print( os.listdir(PATH) )
#print (files[0],'\n',files[1][0].replace(b'\\\\',b'\\'),files[1],'\n',files[3])
if non_printable_dir_name_counter + non_printable_f_name_counter:
    print ("non printable dir names:",non_printable_dir_name_counter,
           "non printable file names:",non_printable_f_name_counter )
    exit(0)
for f in files:
    _path=f[0].encode(OUTPUT_ENCODING,'replace').decode(OUTPUT_ENCODING)
    _f_name= f[1].encode(OUTPUT_ENCODING,'replace').decode(OUTPUT_ENCODING)
    non_printable_dir= _path != f[0]
    non_printable_f_name= _f_name != f[1]
    print (f[0].replace('\\\\','\\').encode('cp1251','replace').decode('cp1251'),
           f[1].encode('cp1251','replace').decode('cp1251'),f[2])
    print(len(files))


