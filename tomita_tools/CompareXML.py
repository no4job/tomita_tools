#coding windows-1251
__author__ = 'mdu'
#import io
#import re
#import operator
#from tomita_tools import Fragments
import codecs
#from io import StringIO
#from datetime import datetime
try:
    from lxml import etree
except ImportError:
    print("lxml import error")
    raise
class ParametersForCompare():
    def __init__(self, **kwargs):
        #absolute or relative path to input reference XML markup file
        self.inputReferenceXMLMarkupFile = kwargs.get('INPUT_REFERENCE_XML_MARKUP_FILE','')
        #absolute or relative path to input reference XML markup file encoding
        self.inputReferenceXMLMarkupFileEncoding = kwargs.get('INPUT_REFERENCE_XML_MARKUP_FILE_ENCODING','')
        #absolute or relative path to input compared XML markup file
        self.inputComparedXMLMarkupFile = kwargs.get('INPUT_COMPARED_XML_MARKUP_FILE','cp1251')
        #absolute or relative path to input compared XML markup file encoding
        self.inputComparedXMLMarkupFileEncoding = kwargs.get('INPUT_COMPARED_XML_MARKUP_FILE_ENCODING','cp1251')
        #absolute or relative path to output file with comparison results
        self.outputComparisonResults = kwargs.get('OUTPUT_COMPARISON_RESULTS','cp1251')

class difElement():
    def __init__(self, **kwargs):
        self.text = kwargs.get('TEXT','')
        self.position = kwargs.get('POSITION',0)
        self.length = kwargs.get('LENGTH',0)
        self.source = kwargs.get('SOURCE','')
#*********************************************************************************



def compare(parameters: ParametersForCompare)-> ParametersForCompare:
    s=""
    #create list reference replacements
    referenceReplacements = {}
    referenceRoot = etree.parse(parameters.inputReferenceXMLMarkupFile)
    referenceReplacementsElements= referenceRoot.xpath(".//facts/descendant-or-self::*[@pos]")

    for replacement in referenceReplacementsElements:
        replacementFragment = difElement()
        replacementFragment.text = replacement.find("ReplacementText").attrib["val"]
        replacementFragment.position = replacement.attrib["pos"]
        replacementFragment.length = replacement.attrib["len"]
        replacementFragment.source = "r"
        key = str(replacementFragment.position).zfill(10)+";"+str(replacementFragment.length).zfill(10)
        referenceReplacements[key]=replacementFragment


    #create list compared replacements
    comparedReplacements = {}
    comparedRoot = etree.parse(parameters.inputComparedXMLMarkupFile)
    comparedReplacementsElements= comparedRoot.xpath(".//facts/descendant-or-self::*[@pos]")
    for replacement in comparedReplacementsElements:
        replacementFragment = difElement()
        replacementFragment.text = replacement.find("ReplacementText").attrib["val"]
        replacementFragment.position = replacement.attrib["pos"]
        replacementFragment.length = replacement.attrib["len"]
        replacementFragment.source = "c"
        key = str(replacementFragment.position).zfill(10)+";"+str(replacementFragment.length).zfill(10)
        comparedReplacements[key]=replacementFragment

    #create list of unmatched replacements
    diffList={}
    for key in referenceReplacements:
        if key not in  comparedReplacements:
            #keyParts = key.split(";")
            diffList[key.split(";")[0]+"0"+key.split(";")[1]]=referenceReplacements[key]
    for key in comparedReplacements:
        if key not in  referenceReplacements:
            diffList[key.split(";")[0]+"1"+key.split(";")[1]]=comparedReplacements[key]

    s=""

    diffListKeys= list(diffList.keys())
    diffListKeys.sort()
    for difListKey in   diffListKeys:
        diff=diffList[difListKey]
        if diff.source == "r":
            source="Reference"
        elif diff.source == "c":
            source="Compared: "
        else:
            source="Uknown: "
        s=s+source+"(pos= "+str(diff.position)+", len= "+str(diff.length)+"): "
        s=s+diff.text+"\n"
    #with open(parameters.outputComparisonResults, "w") as f:
    with codecs.open(parameters.outputComparisonResults, "w", "windows-1251") as f:
        f.write(s)
    return

if __name__ == '__main__':
    p =  ParametersForCompare()
    p.inputReferenceXMLMarkupFile = "out_xml_ref.xml"
    p.inputComparedXMLMarkupFile = "out_xml_cmp.xml"
    p.outputComparisonResults = "compare.txt"
    compare(p)
    exit(0)
