#coding windows-1251
__author__ = 'mdu'
import argparse
from common_config import *
#from tomita_tools import MarkupXML
import MarkupXML
import CompareXML
'''
try:
    import MarkupXML
except ImportError:
    try:
        from tomita_tools import MarkupXML
    except:
        raise

#from tomita_tools import CompareXML
try:
    import CompareXML
except ImportError:
    try:
        from tomita_tools import CompareXML
    except:
        raise
'''


def markupWithArgs (args):
    #output = "markuped file:{0}\noutput text file: {1}\noutput xml file: {2}"
    #output=output.format(args.markupedHTMLFile,args.outputTextFile,args.outputXMLFile)
    #print(output)
    p = MarkupXML.ParametersForMarkup()
    p.inputMarkupedHTMLFile = args.markupedHTMLFile
    p.outputTextFile = args.outputTextFile
    p.outputXMLFile = args.outputXMLFile
    MarkupXML.markup(p)

def compareWithArgs(args):
    #output = "xml file with reference replcacements:{0}\nxml file with parser replacements: {1}\noutput file: {2}"
    #output=output.format(args.referenceXMLFile,args.comparedXMLfile,args.comparisonOutputFile)
    #print(output)
    p = CompareXML.ParametersForCompare()
    p.inputReferenceXMLMarkupFile = args.referenceXMLFile
    p.inputComparedXMLMarkupFile = args.comparedXMLfile
    p.outputComparisonResultsFile = args.comparisonOutputFile
    if args.ntq:
        p.trimQuotes = 0
    CompareXML.compare(p)

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='1.0.0')
subparsers = parser.add_subparsers()

markup_parser = subparsers.add_parser('m')
markup_parser.add_argument('markupedHTMLFile', help='absolute or relative path to input markuped html file')
markup_parser.add_argument('outputTextFile', help='absolute or relative path to output text file')
markup_parser.add_argument('outputXMLFile', help='absolute or relative path to output xml file')
markup_parser.set_defaults(func=markupWithArgs)

compare_parser = subparsers.add_parser('c')
compare_parser.add_argument('referenceXMLFile', help='absolute or relative path to xml file with reference '
                                                     'replacements')
compare_parser.add_argument('comparedXMLfile', help='absolute or relative path to compared xml file with replacements')
compare_parser.add_argument('comparisonOutputFile', help='absolute or relative path to output file with comparison '
                                              'results')
#compare_parser.add_argument('--tq', action='store_true', help='Enable trim edge quotes and replace non-edge quotes to spaces in reference replacements before comparison')
compare_parser.add_argument('--ntq', action='store_true', help='Disable trim edge quotes and replace non-edge quotes to spaces in reference replacements before comparison')
compare_parser.set_defaults(func=compareWithArgs)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)