__author__ = 'MishninDY'
import sys, getopt
import codecs
from itertools import combinations
# with codecs.open(parameters.outputComparisonResultsFile, encoding=parameters.outputComparisonResultsFileEncoding,mode="w") as f:
#     f.write(s)
# return
def split_combine(input_file,output_file,file_encoding):
    splitted =[]
    with codecs.open(input_file, encoding = file_encoding,mode="r") as fi:
        for line in fi:
            #styleSection = re.findall(r"<\s*style\s*>.*<\!--.*-->\s*<\s*/\s*style\s*>", s,flags=re.IGNORECASE)
            if (file_encoding == "utf8"):
                //line_filtered = line.replace(br'\xc2\xa0',u' ')
                line_filtered = findall(line," ")
            if (file_encoding == "cp1251"):
                line_filtered = line.replace(u'\xa0', u' ')
            line_elements = line_filtered.split(" ")
            for i in range(1, len(line_elements)+1):
                combination = combinations(line_elements, i)
                for j in range(1, len(combination)+1):
                    combination_str = " ".join(combination)
                    splitted.append(combination_str)
    # with codecs.open(output_file, encoding = file_encoding, mode="w") as fo:
    #     for element in splitted:
    #         fo.write("%s\n" %element)


#def main(argv):
if __name__ == '__main__':
    inputfile = "C:\\tomita_project\\CarMakeModel\\input\\series.txt"
    outputfile = "C:\\tomita_project\\CarMakeModel\\input\\series_splitted.txt"
    encoding = "utf8";
    # inputfile = ''
    # outputfile = ''
    # try:
    #     opts,args = getopt.getopt(argv,"wuh")
    # except getopt.GetoptError:
    #     print ('split [encoding] <inputfile> <outputfile>')
    #     sys.exit(2)
    # for opt in opts:
    #     if opt == '-u':
    #         encoding = 'utf8'
    #     elif opt == '-w':
    #         encoding = 'cp1251'
    #     if opt == '-h':
    #         print ('split [encoding -u or -w  (utf8 or cp1251)] <inputfile> <outputfile>')
    #         sys.exit(0)
    #     else:
    #         encoding = 'utf8'
    # if (len(opts)== 1 and len(args)== 4):
    #     inputfile = args[2]
    #     outputfile = args[3]
    # elif(len(opts)== 0 and len(args)== 2):
    #     inputfile = args[1]
    #     outputfile = args[2]
    # else:
    #     print ('split [encoding -u or -w  (utf8 or cp1251)] <inputfile> <outputfile>')
    #     sys.exit(2)
    split_combine(inputfile,outputfile,encoding)
    exit(0)