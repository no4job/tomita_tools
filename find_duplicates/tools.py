__author__ = 'mdu'
import os
import datetime
import tempfile

from unidecode import unidecode


def non_printable(s,encoding):
    result = []
    for i, c in enumerate(s):
        c_recoded = c.encode(encoding,'replace').decode(encoding)
        if c_recoded != c:
            result += [i]
    return result

def translit_on_positions(s,positions):
    _s=list(s)
    for i in positions:
        _s[i]=unidecode(_s[i])
    return "".join(_s)

def translit_non_printable(s,encoding):
    return translit_on_positions(s,non_printable(s,encoding))

def translit_non_printable_dir_name(s,encoding):
    return os.path.join(os.path.split(s)[0],
        translit_non_printable(os.path.split(s)[1],encoding))

def translit_non_printable_f_name(s,encoding):
    return translit_non_printable_dir_name(s,encoding)

def create_log_file(path):
    now_time = datetime.datetime.now()
    _prefix="rename_log_"+now_time.strftime("%d_%m_%y_%H_%M_%S")+"_"
    _suffix=".txt"
    return tempfile.NamedTemporaryFile(mode="w+", suffix=_suffix,prefix=_prefix, dir=path, delete=False, encoding="utf-8")

def rename_if_exist(t,name):
    _name=name
    sfx=1
    if t=="d":
        while os.path.isdir(_name):
            _name=name+"("+str(sfx)+")"
            sfx+=1
    elif t=="f":
        while os.path.isfile(_name):
            fileName, fileExtension = os.path.splitext(_name)
            _name=fileName+"("+str(sfx)+")"+fileExtension
            sfx+=1
    return _name
