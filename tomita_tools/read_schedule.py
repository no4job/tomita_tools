__author__ = 'mdu'

try:
    from lxml import etree
except ImportError:
    print("lxml import error")
    raise
with open("xmltv.xml",encoding="utf8", mode="r") as f:
    s=f.read()
    #******* step 2: get <body> element from clean string
    parser = etree.HTMLParser()
    #doc_tree = etree.parse(os.path.join(os.getcwd(),"test.htm"),parser)
    doc_tree = etree.parse(StringIO(s),parser)#parse string cleaned from \n as io stream
    root = doc_tree.getroot()
    body = doc_tree.find('body')
    #******* step 4: create  css markup dictionary {element, nearest outer element with markup css class attribute}
    elementsWithCSSClass=body.xpath("descendant-or-self::*[@class]")#list of all elements with css class attribute
    elementsWithMarkupCSSClass=[]#***list of elements with markup css class attribute
    for element in elementsWithCSSClass:
        if re.match(cssMarkupClassNamePattern,element.attrib["class"]):
            elementsWithMarkupCSSClass.append(element)

    s=""
    for element in textElements:
        s=s+element[0]
    #with open("out_text.txt", "w") as f:
    with open(parameters.outputTextFile,encoding=parameters.outputTextFileEncoding,mode= "w") as f:
        f.write(s)