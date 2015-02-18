__author__ = 'mdu'
from tools import *


#Tool settings
PATH = "K:\\"
#PATH = "K:\\"+"tmp"
OUTPUT_ENCODING='cp1251'
CHECK=True
#RENAME=True
RENAME=False
LOG_CHANGES=True
LOG_FILE_PATH=PATH
# open log file for non printable names and their transliterated versions
log_file = create_log_file(LOG_FILE_PATH)

#check entry point path for non printable characters
non_printable_positions=non_printable(PATH,OUTPUT_ENCODING)
if non_printable_positions:
    print ("Entry point path includes non printable characters:",
           non_printable_positions, PATH.encode('cp1251','replace').decode('cp1251'))

# check recursively for non printable characters
files=[]
non_printable_dir_name_counter = 0
non_printable_f_name_counter = 0
print("Start")
# traverse all dirs and files recursively
for dir in os.walk(top=PATH, topdown=False):
    # test and rename file names
    for f_name in dir[2]:
        non_printable_positions=non_printable(f_name,OUTPUT_ENCODING)
        if (non_printable_positions):
            t_f_name=translit_non_printable_f_name(f_name,OUTPUT_ENCODING)
            t_f_name=os.path.split(rename_if_exist("f",os.path.join(dir[0],t_f_name)))[1]
            if LOG_CHANGES:
                log_file.write("f"+";"+",".join((str(i) for i in non_printable_positions))+";"+dir[0]+";"+
                               ";"+f_name+";"+t_f_name+"\n")
            print ("f:",non_printable_positions,
                   dir[0].replace('\\\\', '\\').encode('cp1251','replace').decode('cp1251'),
                   " : ",
                   f_name.replace('\\\\', '\\').encode('cp1251','replace').decode('cp1251'),
                   " -> ",
                   t_f_name)
            non_printable_f_name_counter+=1
            if RENAME:
                os.rename(os.path.join(dir[0],f_name),os.path.join(dir[0],t_f_name))
    # test and rename directory names
    for _dir_name in dir[1]:
        non_printable_positions=non_printable(_dir_name,OUTPUT_ENCODING)
        dir_name=os.path.join(dir[0],_dir_name)
        if (non_printable_positions):
            t_dir_name=translit_non_printable_dir_name(dir_name,OUTPUT_ENCODING)
            t_dir_name=rename_if_exist("d",t_dir_name)
            if LOG_CHANGES:
                log_file.write("d"+";"+",".join((str(i) for i in non_printable_positions))+";"+dir_name+";"+t_dir_name+"\n")
            print ("d:",non_printable_positions,
                   dir_name.replace('\\\\', '\\').encode('cp1251','replace').decode('cp1251'),
                   " -> ",
                   t_dir_name.replace('\\\\', '\\').encode('cp1251','replace').decode('cp1251'))
            non_printable_dir_name_counter+=1
            if RENAME:
                os.rename(dir_name,t_dir_name)

print("End")
if non_printable_dir_name_counter + non_printable_f_name_counter:
    print ("non printable dir names:",non_printable_dir_name_counter,
           "\n"+"non printable file names:",non_printable_f_name_counter )
else:
    print ("all names are printable")
log_file.close()
exit(0)


