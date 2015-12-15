#coding windows-1251
__author__ = 'mdu'
#import io
#import re
#import operator
#from tomita_tools import Fragments
import codecs
import os.path
#from io import StringIO
#from datetime import datetime
from common_config import *
try:
    from lxml import etree
except ImportError:
    print("lxml import error")
    raise
class ParametersForCompare():
    def __init__(self, **kwargs):
        #absolute or relative path to input reference XML markup file
        self.inputReferenceXMLMarkupFile = kwargs.get('INPUT_REFERENCE_XML_MARKUP_FILE','')
        #input reference XML markup file encoding
        self.inputReferenceXMLMarkupFileEncoding = kwargs.get('INPUT_REFERENCE_XML_MARKUP_FILE_ENCODING',\
                                                              DEFAULT_INPUT_REFERENCE_XML_FILE_ENCODING)
        #absolute or relative path to input compared XML markup file
        self.inputComparedXMLMarkupFile = kwargs.get('INPUT_COMPARED_XML_MARKUP_FILE',\
                                                     '')
        #input compared XML markup file encoding
        self.inputComparedXMLMarkupFileEncoding = kwargs.get('INPUT_COMPARED_XML_MARKUP_FILE_ENCODING', \
                                                             DEFAULT_INPUT_COMPARED_XML_FILE_ENCODING)
        #absolute or relative path to output file with comparison results
        self.outputComparisonResultsFile = kwargs.get('OUTPUT_COMPARISON_RESULTS','')

        #output file with comparison results
        self.outputComparisonResultsFileEncoding = kwargs.get('OUTPUT_COMPARISON_RESULTS',\
                                                              DEFAULT_OUTPUT_COMPARISON_TXT_FILE_ENCODING)
        #to trim or not to trim quotes in reference markup text
        self.trimQuotes = kwargs.get('TRIM_QUOTES',1)
class difElement():
    def __init__(self, **kwargs):
        self.text = kwargs.get('TEXT','')
        self.position = kwargs.get('POSITION',0)
        self.length = kwargs.get('LENGTH',0)
        self.source = kwargs.get('SOURCE','')
#*********************************************************************************

def getPathFromParrentLevel(inputPath,level):
    path=""
    up=0
    while up<=level:
        head, tail = os.path.split(inputPath)
        inputPath = head
        if up!=0:
            path = os.path.join(tail,path)
        else:
            path=tail
        up+=1
    return path

def compare(parameters: ParametersForCompare)-> ParametersForCompare:
    s=""
    trimCount=0;
    #create list reference replacements
    referenceReplacements = {}
    #**parse according to encoding in XML declaration
    referenceRoot = etree.parse(parameters.inputReferenceXMLMarkupFile)
    referenceReplacementsElements= referenceRoot.xpath(".//facts/descendant-or-self::*[@pos]")

    for replacement in referenceReplacementsElements:
        replacementFragment = difElement()
        replacementFragment.text = replacement.find("ReplacementText").attrib["val"]
        replacementFragment.position = replacement.attrib["pos"]
        replacementFragment.length = replacement.attrib["len"]
        replacementFragment.source = "r"
    #special case: trim leading and trailing quotes in reference replacements
    #  for compatibility with tomita XML output
        trimFlag=0
        if parameters.trimQuotes :
            if replacementFragment.text[0] in ('"',"'","«",'“','”',"‘","’"):
                trimFlag=1
                replacementFragment.text = replacementFragment.text[1:]
                replacementFragment.position = str(int(replacementFragment.position) + 1)
                replacementFragment.length = str(int(replacementFragment.length) - 1)
            if replacementFragment.text[-1:] in ('"',"'","»",'“','”',"‘","’"):
                trimFlag=1
                replacementFragment.text=replacementFragment.text[:-1]
                replacementFragment.length = str(int(replacementFragment.length) - 1)
            for chr in ('"',"'","«","»",'“','”',"‘","’"):
                if chr in replacementFragment.text:
                    trimFlag=1
                replacementFragment.text=replacementFragment.text.replace(chr," ")
        trimCount+=trimFlag
        key = str(replacementFragment.position).zfill(10)+";"+str(replacementFragment.length).zfill(10)
        referenceReplacements[key]=replacementFragment


    #create list compared replacements
    comparedReplacements = {}
    #**parse according to encoding in XML declaration
    comparedRoot = etree.parse(parameters.inputComparedXMLMarkupFile)
    comparedReplacementsElements= comparedRoot.xpath(".//facts/descendant-or-self::*[@pos]")
    try:
        for replacement in comparedReplacementsElements:
            replacementFragment = difElement()
            replacementFragment.text = replacement.find("ReplacementText").attrib["val"]
            replacementFragment.position = replacement.attrib["pos"]
            replacementFragment.length = replacement.attrib["len"]
            replacementFragment.source = "c"
            key = str(replacementFragment.position).zfill(10)+";"+str(replacementFragment.length).zfill(10)
            comparedReplacements[key]=replacementFragment
    except AttributeError:
        print("No mandatory fields in parser output XML file, check parser facts extracting  settings")
        exit(1)
        #raise
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
    referenceUnmatched=0
    comparedUnmatched=0
    unknown=0
    diffListKeys= list(diffList.keys())
    diffListKeys.sort()
    for difListKey in   diffListKeys:
        diff=diffList[difListKey]
        if diff.source == "r":
            source="Reference"
            referenceUnmatched+=1
        elif diff.source == "c":
            source="Compared: "
            comparedUnmatched+=1
        else:
            source="Uknown: "
            unknown+=1
        s=s+source+"(pos= "+str(diff.position)+", len= "+str(diff.length)+"): "
        s=s+diff.text+"\n"

    print("Refference file: "+ getPathFromParrentLevel(parameters.inputReferenceXMLMarkupFile,2))
    print("Compared file: "+ getPathFromParrentLevel(parameters.inputComparedXMLMarkupFile,2)+"\n")
    print("Reference file replacements number:"+str(len(referenceReplacementsElements))+", unmatched: "+str(referenceUnmatched))
    print("Compared  file replacements number:"+str(len(comparedReplacementsElements))+", unmatched: "+str(comparedUnmatched))
    if parameters.trimQuotes:
        print("Quotes trim enabled (in reference), trimmed: "+str(trimCount))
    s= s+"\n"+"Reference file: "+ getPathFromParrentLevel(parameters.inputReferenceXMLMarkupFile,2)
    s= s+"\n"+"Compared  file: "+ getPathFromParrentLevel(parameters.inputComparedXMLMarkupFile,2)
    s= s+"\n"+"Reference file replacements number:"+str(len(referenceReplacementsElements))+", unmatched: "+str(referenceUnmatched)
    s= s+"\n"+"Compared  file replacements number:"+str(len(comparedReplacementsElements))+", unmatched: "+str(comparedUnmatched)
    if parameters.trimQuotes:
        s= s+"\n"+"Quotes trim enabled (in reference), trimmed: "+str(trimCount)

    #print(os.path.basename(parameters.inputReferenceXMLMarkupFile))
    #os.path.split

    #with open(parameters.outputComparisonResults, "w") as f:
    with codecs.open(parameters.outputComparisonResultsFile, encoding=parameters.outputComparisonResultsFileEncoding,mode="w") as f:
        f.write(s)
    return

if __name__ == '__main__':
    p =  ParametersForCompare()
    p.inputReferenceXMLMarkupFile = "C:\\tomita_project\\Address\\input\\test_0068.xml"
    p.inputComparedXMLMarkupFile = "C:\\tomita_project\\Address\\output\\output.test_0068.xml"
    p.outputComparisonResultsFile = "C:\\tomita_project\\Address\\output\\dif.test_0068_.txt"
    compare(p)
    exit(0)
