#coding windows-1251
__author__ = 'mdu'
import argparse

def markup(args):
    output = "markuped file:{0}\noutput text file: {1}\noutput xml file: {2}"
    output=output.format(args.markupedHTMLFile,args.outputTextFile,args.outputXMLFile)
    print(output)

def compare(args):
    output = "xml file with reference replcacements:{0}\nxml file with parser replacements: {1}\noutput file: {2}"
    output=output.format(args.referenceXMLFile,args.comparedXMLfile,args.comparisonOutputFile)
    print(output)


parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='1.0.0')
subparsers = parser.add_subparsers()

markup_parser = subparsers.add_parser('markup')
markup_parser.add_argument('markupedHTMLFile', help='absolute or relative path to markuped html file')
markup_parser.add_argument('outputTextFile', help='absolute or relative path to output text file')
markup_parser.add_argument('outputXMLFile', help='absolute or relative path to output xml file')
markup_parser.set_defaults(func=markup)

compare_parser = subparsers.add_parser('compare')
compare_parser.add_argument('referenceXMLFile', help='absolute or relative path to xml file with reference '
                                                     'replacements')
compare_parser.add_argument('comparedXMLfile', help='absolute or relative path to compared xml file with replacements')
compare_parser.add_argument('comparisonOutputFile', help='absolute or relative path to output file with comparison '
                                              'results')
compare_parser.set_defaults(func=compare)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)