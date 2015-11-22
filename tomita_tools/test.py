#coding windows-1251
__author__ = 'mdu'
import os
import io
import re
from io import StringIO

try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")

#parser = etree.HTMLParser()
#tree = etree.parse(os.path.join(os.getcwd(),"test_1u.htm"), parser)
#print (etree.tostring(tree.getroot(), pretty_print=True))
#print(etree.tostring(tree))
'''
def iterateTextElements(element,textElements):
    if element.text != None:
        element.
        #textElements
'''
# ******* read word markup style names from cofig file
styleList=[]
with io.open(file="StylesList.txt", encoding="cp1251",mode="rt") as f:
    for s in f.read().splitlines():
        styleList.append(s.split(","))
#******* map markup css class names and markup style names in html file
s=""
with open("test.htm", "r") as f:
    s=f.read()
classStyleMap={}
for style in styleList:
    className = re.findall('(\w+)[\s\n]*\{[^\{]*'+style[0].replace("/","\\\\/")+'\W*;', s,flags=re.DOTALL | re.IGNORECASE)
    classStyleMap[style[0]]=className[0] if len(className)> 0 else ""

print(classStyleMap)
#******* map text element and parent markup css class
#******* remove \n from html
with open("test.htm", "r") as f:
    s=re.sub("[\n]+","",f.read())
    print (s)
parser = etree.HTMLParser()
#doc_tree = etree.parse(os.path.join(os.getcwd(),"test.htm"),parser)
doc_tree = etree.parse(StringIO(s),parser)
root = doc_tree.getroot()
body = doc_tree.find('body')
textElements=[]
#*****create css markup class name pattern
cssMarkupClassNamePattern=""
for className in classStyleMap:
    cssMarkupClassNamePattern+=(classStyleMap[className]+"|")
cssMarkupClassNamePattern=cssMarkupClassNamePattern[:-1]
#******create  css markup dictionary for elements
elementsWithCSSClass=body.xpath("descendant-or-self::*[@class]")
elementsWithMarkupCSSClass=[]
for element in elementsWithCSSClass:
    if re.match(cssMarkupClassNamePattern,element.attrib["class"]):
        elementsWithMarkupCSSClass.append(element)
markupedElements={}
#markupedElement={}
for elementWithMarkupCSSClass in elementsWithMarkupCSSClass:
    for element in elementWithMarkupCSSClass.xpath("descendant-or-self::*"):
        markupedElements[element]=elementWithMarkupCSSClass
        #markupedElements[element]=elementWithMarkupCSSClass.attrib["class"]
#exit(0)
#******search css markup class name for each text element

def iterateTextElements(element,textElements,markupedElements):
    textElement=[]
    if element.text != None:
        textElement.append(element.text)
        textElement.append(markupedElements.get(element))
        textElements.append(textElement)
    for childElement in element:
        iterateTextElements(childElement,textElements,markupedElements)
    textElement=[]
    if element.tail != None:
        textElement.append(element.tail)
        textElement.append(markupedElements.get(element))
        textElements.append(textElement)

textElements=[]
iterateTextElements(body,textElements,markupedElements)
#******create text file
s=""
for element in textElements:
    s=s+element[0]
with open("out_text.txt", "w") as f:
    f.write(s)


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