__author__ = 'mdu'
from datetime import *
try:
    from lxml import etree
except ImportError:
    print("lxml import error")
    raise

def getDateTime(dateTimeStr):
    year=int(dateTimeStr[0:4])
    month=int(dateTimeStr[4:6])
    day=int(dateTimeStr[6:8])
    hour=int(dateTimeStr[8:10])
    minute=int(dateTimeStr[10:12])
    second=int(dateTimeStr[12:14])
    return datetime(year, month, day, hour, minute, second)
def getDateStr(dateTimeStr):
    year=dateTimeStr[0:4]
    month=dateTimeStr[4:6]
    day=dateTimeStr[6:8]
    return day+"."+month+"."+year
def getTimeStr(dateTimeStr):
    hour=dateTimeStr[8:10]
    minute=dateTimeStr[10:12]
    second=dateTimeStr[12:14]
    return hour+":"+minute+":"+second
def getDateTimeStr(dateTimeStr):
    return getDateStr(dateTimeStr)+" "+getTimeStr(dateTimeStr)
def getTimeDelta(startDateTime,stopDateTime):
    delta=stopDateTime - startDateTime
    return int(delta.total_seconds())
def norm(inputStr):
    return inputStr.replace("\t"," ").replace("\n"," ").strip()

with open("xmltv_channels.csv",encoding="utf8", mode="w") as f:
    f.write("%s\t%s\t%s\n" %("channel_id","display_name","icon"))
    for action, element in etree.iterparse("xmltv.xml"):
        if element.tag=="channel":
            channel_id=norm(element.attrib["id"])
            display_name=""
            icon=""
            for childElement in list(element):
                if childElement.tag=="display-name":
                    display_name=norm(childElement.text)
                if childElement.tag=="icon":
                    icon=childElement.attrib["src"]
            f.write("%s\t%s\t%s\n" %(channel_id,display_name,icon))


with open("xmltv_schedule.csv",encoding="utf8", mode="w") as f:
    f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %("channel_id","start","stop","delta","title","desc","category"))
    for action, element in etree.iterparse("xmltv.xml"):
        if element.tag=="programme":
            start=""
            stop=""
            channel=""
            startStr=norm(str.split(element.attrib["start"])[0])
            stopStr=norm(str.split(element.attrib["stop"])[0])
            start=getDateTimeStr(startStr)
            stop=getDateTimeStr(stopStr)
            delta=getTimeDelta(getDateTime(startStr),getDateTime(stopStr))
            channel_id=norm(str.split(element.attrib["channel"])[0])
            #print("%s, %s" % (start,stop))
            #print("%s, %s" % (str.split(element.attrib["start"])[0],str.split(element.attrib["stop"])[0]))
            title=""
            desc=""
            category=""
            for childElement in list(element):
                if childElement.tag=="title":
                    title=norm(childElement.text)
                if childElement.tag=="desc":
                    desc=norm(childElement.text)
                if childElement.tag=="category":
                    category=norm(childElement.text)
            f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %(channel_id,start,stop,delta,title,desc,category))
