#coding windows-1251
__author__ = 'mdu'
import os
import io
import re
from tomita_tools import Fragments
from io import StringIO


try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
 pass


# ******* read word markup style names from config file
styleList=[] # list of lists [markup style name, marup style ID]
with io.open(file="StylesList.txt", encoding="cp1251",mode="rt") as f:
    for s in f.read().splitlines():
        styleList.append(s.split(","))
#******* map markup css class names and markup style names in html file
s=""
with open("test.htm", "r") as f:
    s=f.read()
styleClassMap={}#***dictionary {markup style name, markup css class name}
classStyleMap={}#***dictionary {markup css class name,markup style name}
for style in styleList:
    className = re.findall('(\w+)[\s\n]*\{[^\{]*'+style[0].replace("/","\\\\/")+'\W*;', s,flags=re.DOTALL | re.IGNORECASE)
    styleClassMap[style[0]]=className[0] if len(className)> 0 else ""
    if len(className)>0:
        classStyleMap[className[0]]= style[0]
#print(styleClassMap)
#******* map text element and parent markup css class
#******* step 1: remove \n from html
with open("test.htm", "r") as f:
    s=f.read()
#*** special case: \n inside tag replcacing with " "
    while True:
        tagBreaks=re.findall("(<[^<^>]*)([\n])([^<^>]*>)",s)
        if len(tagBreaks)== 0:
            break
        for tagBreak in tagBreaks:
            searchPattern = tagBreak[0]+tagBreak[1]+tagBreak[2]
            s=s.replace(searchPattern,tagBreak[0]+" "+tagBreak[2])
#*** common case: \n between tag replcacing with ""
    #print (s)
    s=re.sub("[\n]+","",s)
#    print (s)
#******* step 2: get <body> element from clean string
parser = etree.HTMLParser()
#doc_tree = etree.parse(os.path.join(os.getcwd(),"test.htm"),parser)
doc_tree = etree.parse(StringIO(s),parser)#parse string cleaned from \n as io stream
root = doc_tree.getroot()
body = doc_tree.find('body')
print (etree.tostring(body, pretty_print=True))
#******* step 3: create string with search pattern from css markup class names
cssMarkupClassNamePattern=""
for className in styleClassMap:
    cssMarkupClassNamePattern+=(styleClassMap[className]+"|")
cssMarkupClassNamePattern=cssMarkupClassNamePattern[:-1]

#******* step 4: create  css markup dictionary {element, nearest outer element with markup css class attribute}
elementsWithCSSClass=body.xpath("descendant-or-self::*[@class]")#list of all elements with css class attribute
elementsWithMarkupCSSClass=[]#***list of elements with markup css class attribute
for element in elementsWithCSSClass:
    if re.match(cssMarkupClassNamePattern,element.attrib["class"]):
        elementsWithMarkupCSSClass.append(element)
markupedElements={}#***dictionary {element, nearest outer element with markup css class attribute}
#markupedElement={}
for elementWithMarkupCSSClass in elementsWithMarkupCSSClass:
    for element in elementWithMarkupCSSClass.xpath("descendant-or-self::*"):
        markupedElements[element]=elementWithMarkupCSSClass
        #markupedElements[element]=elementWithMarkupCSSClass.attrib["class"]
#exit(0)




#******* step 5: extract text  from markuped elements and map them with css markup elements

#***function return list of lists where each list contain:
#  [text or tail, nearest outer element with markup css class attribute]
#  texts/tails ordered as in the parsed document
def iterateTextElements(element,textElements,markupedElements):
    textElement=[]
    if element.text != None:
        #***create list of 2 elemets - [text of element ,nearest outer element with markup css class attribute]
        textElement.append(element.text)
        textElement.append(markupedElements.get(element))
        #***append above list to list of lists
        textElements.append(textElement)
    #***recursive iterate over child elements
    for childElement in element:
        iterateTextElements(childElement,textElements,markupedElements)
        textElement=[]
        if childElement.tail != None:
            #***create list of 2 elemets - [tail of element ,nearest outer element with markup css class attribute]
            textElement.append(childElement.tail)
            textElement.append(markupedElements.get(element))
            #***append above list to list of lists
            textElements.append(textElement)

textElements=[]#***list of lists where each list contain text or tail in the order as in the parsed document
iterateTextElements(body,textElements,markupedElements)

#******* step 6: create output text file
s=""
for element in textElements:
    s=s+element[0]
with open("out_text.txt", "w") as f:
    f.write(s)

#******* step 7: create output XML file

replacements=[]
length=0
position = 0
for element in textElements:
    if element[1] != None:
        kw={}
        kw["TEXT"]=element[0]
        kw["LENGTH"]=len(element[0])
        kw["POSITION"]=position
        position+=len(element[0])
        kw["MARKUP_STYLE_NAME"]=classStyleMap.get(element[1].attrib["class"])
        kw["MARKUP_CSS_CLASS_NAME"]=element[1].attrib["class"]
        kw["PATH_TO_ELEMENT_WITH_CSS_MARKUP"]=doc_tree.getpath(element[1])
        r=Fragments.Replacement(**kw)
        replacements.append(r)
exit(0)




'''
for element in body.iter():
    #if
    parentsWithCSS=element.xpath("ancestor::*[@class]")
    for parent in parentsWithCSS:
        if re.match(cssMarkupClassNamePattern,parent.attrib["class"]):
            print("%s - %s" % (element.tag,parent.attrib["class"]))
    #if element.xpath("ancestor::*[@classs]") != None and :
     #   pass

    print("%s-%s",(element.tag,element.text))
print(ancestor)
    #print(element.text if element.text!=None else "",sep="")
#print(allMarkUpNodes)
'''