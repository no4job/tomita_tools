__author__ = 'mdu'
import datetime
try:
    from lxml import etree
except ImportError:
    print("lxml import error")
    raise
from datetime import datetime
import sys
sys.path.append("C:\IdeaProjects\tomita_tools\MongoTest")
from Timer import *

def get_model_element(elem):
    modelElement={}
    #*****************************
    modelElement["parent_object"]=""
    modelElement["model_revision"]=""
    modelElement["description"]=""
    modelElement["native_id"]=""
    modelElement["creation_date"]=datetime.now()
    modelElement["change_date"]=datetime.now()
    modelElement["archive"]="false"
    modelElement["deleted"]="false"
    #***************************************************

    modelElement["name"]=next(iter(elem.xpath("./@ElementName")),"")
    modelElement["id"]=next(iter(elem.xpath("./@ElementId")),"")
    modelElement["type"]=next(iter(elem.xpath("./@TypeID")),"")
    data_section_2=[]
    for attributeElement in elem.xpath("./www.qpr.com:Attribute",namespaces={'www.qpr.com': 'www.qpr.com'}):
        fieldName=next(iter(attributeElement.xpath("./@AttributeName")),"")
        field={}
        field_values_array=[]
        valueArray=[]
        valueArray.extend(attributeElement.xpath("./www.qpr.com:Value/text()",namespaces={'www.qpr.com': 'www.qpr.com'}))
        if len(valueArray):
            field_values_array.append(dict(Value=valueArray))
        records=[]
        for recordElement in attributeElement.xpath("./www.qpr.com:Record",namespaces={'www.qpr.com': 'www.qpr.com'}):
            #record=[]
            record={}
            for recordFieldElement in recordElement.xpath("./www.qpr.com:Field",namespaces={'www.qpr.com': 'www.qpr.com'}):
                recordFieldName=next(iter(recordFieldElement.xpath("./@Name")),"")
                recordFieldValue=next(iter(recordFieldElement.xpath("./@Value")),"")
                #recordField={}
                #recordField[recordFieldName]=recordFieldValue
                #record.append(recordField)
                record[recordFieldName]=recordFieldValue
            records.append(record)
        if len(records):
            field_values_array.append(dict(Record=records))
        field[fieldName]=field_values_array
        data_section_2.append(field)
    modelElement["data_section_2"]=data_section_2
    return modelElement
def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

if __name__ == '__main__':
    t = Timer()
    t.start()

    #input_file='C:\\IdeaProjects\\hh_api_test\\MongoTest\\exp_types_formatted_few_elements.xml'
    #***input_file='exp_types_formatted_few_elements.xml'
    input_file='C:\\Users\mdu\\Documents\\qpr_export\\exp.xml'
    #input_file='C:\\Users\mdu\\Documents\\qpr_export\\exp_types_formatted_few_elements_dots.xml'
    #***input_file='C:\\Users\МишинДЮ\\Documents\\qpr_export\\exp.xml'
    events = ("start", "end")
    context = etree.iterparse(input_file,events = events, tag=('{www.qpr.com}ModelElement'))
    count=0
    dot_key_count=0
    key_count=0
    elements_with_dot_count=0
    # key_path="./descendant-or-self::Attribute/Record/Field/@Name[contains(., '.')]|" \
    #          "./descendant-or-self::*/@AttributeName[# contains(., '.')]"
    key_path_1="./www.qpr.com:Attribute/www.qpr.com:Record/www.qpr.com:Field[@Name[contains(., '.')]]"
    key_path_1_c="./www.qpr.com:Attribute/www.qpr.com:Record/www.qpr.com:Field/@Name"
    key_path_2="./www.qpr.com:Attribute[@AttributeName[contains(., '.')]]"
    key_path_2_c="./www.qpr.com:Attribute/@AttributeName"
    #key_path="./www.qpr.com:Attribute/www.qpr.com:Record/www.qpr.com:Field"
    dot_keys_index=[]
    dot_keys={}
    for action, elem in context:
        if action=="end":
            count+=1
            #print(elem.attrib["ElementName"])
            tree = etree.ElementTree(elem)
            key_count+=int(elem.xpath("count("+key_path_1_c+")",namespaces={'www.qpr.com': 'www.qpr.com'}))
            for attributeElement in elem.xpath(key_path_1,namespaces={'www.qpr.com': 'www.qpr.com'}):
                dot_element_path=str(tree.getelementpath(attributeElement))
                dot_element_attribute=str(attributeElement.attrib["Name"])
                dot_element= "{{www.qpr.com}}ModelElement[{}]/".format(count)+dot_element_path+"/@"+dot_element_attribute
                dot_keys_index.append(dot_element)
                dot_keys[dot_element]=list([dot_element_path])
                #dot_keys[dot_element].append(str(attributeElement.attrib["Name"]))
                dot_keys[dot_element].append(dot_element_attribute)
                dot_key_count+=1
            key_count+=int(elem.xpath("count("+key_path_2_c+")",namespaces={'www.qpr.com': 'www.qpr.com'}))
            for attributeElement in elem.xpath(key_path_2,namespaces={'www.qpr.com': 'www.qpr.com'}):
                dot_element_path=str(tree.getelementpath(attributeElement))
                dot_element_attribute=str(attributeElement.attrib["AttributeName"])
                dot_element= "{{www.qpr.com}}ModelElement[{}]/".format(count)+dot_element_path+"/@"+dot_element_attribute
                dot_keys_index.append(dot_element)
                dot_keys[dot_element]=list([dot_element_path])
                dot_keys[dot_element].append(dot_element_attribute)
                #dot_element=str(tree.getelementpath(attributeElement))+str(attributeElement.attrib["AttributeName"])
                dot_key_count+=1
            if count % 1000  == 0 or count==1:
                print(count)
                t.stop()
                print(t.elapsed)
                t.reset()
                t.start()
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]
        # if count>=1000:
        #     break
    del context
    uniq_dot_keys=uniq(dot_keys[i][1]for i in dot_keys)

    print("Total ModelElement:{}".format(count))
    print("Total key attributes:{}".format(key_count))
    print("Key attributes with dots:{}".format(dot_key_count))
    print("Unique Key attributes with dots:{}".format(len(uniq(dot_keys[i][1]for i in dot_keys))))
    test_cont=0
    for i in dot_keys:
        if dot_keys[i][1] in uniq_dot_keys:
            test_cont+=1
    print("Test = Key attributes with dots:{}".format( test_cont))
    #exit (0)
    context = etree.iterparse(input_file,events = events, tag=('{www.qpr.com}ModelElement'))
    #attr_path='.//*/@*[not(name()="AttributeName" or name()="Name")]'
    attr_path='.//@*[ not(name()="Name" or name()="AttributeName")]'
    value_path='.//www.qpr.com:Value/text()'
    #attr_path='.//*/@*'
    dot_keys_in_values_count_values=0
    dot_keys_in_values_count_attributes=0
    cmp_count=0
    key_count_attributes=0
    key_count_values=0
    #key_count=0
    for action, elem in context:
        if action=="end":
            cmp_count+=1
            key_count_attributes+=int(elem.xpath("count("+attr_path+")",namespaces={'www.qpr.com': 'www.qpr.com'}))
            #print("key_count:{}".format(key_count))
            for attributeElement in elem.xpath(attr_path,namespaces={'www.qpr.com': 'www.qpr.com'}):
                #print(attributeElement)
                if str(attributeElement) in  uniq_dot_keys:
                    dot_keys_in_values_count_attributes+=1
            key_count_values+=int(elem.xpath("count("+value_path+")",namespaces={'www.qpr.com': 'www.qpr.com'}))
            for attributeElement in elem.xpath(value_path,namespaces={'www.qpr.com': 'www.qpr.com'}):
                #print(attributeElement)
                if str(attributeElement) in  uniq_dot_keys:
                    dot_keys_in_values_count_values+=1

            if cmp_count % 100  == 0 or count==1:
                print(cmp_count)
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]
                # if cmp_count>=1000:
                #     break
    del context
    #print("Tect =Total key attributes:{}".format(key_count))
    print("Total key attributes:{}".format(key_count))
    print("Key attributes with dots:{}".format(dot_key_count))
    print("Not Key attributes:{}".format(key_count_attributes))
    print("Value elements:{}".format(key_count_values))
    print("Not Key attributes contains  Key attributes with dots:{}".format(dot_keys_in_values_count_attributes))
    print("Values contains  Key attributes with dots:{}".format(dot_keys_in_values_count_values))
    t.stop()
    print(t.elapsed)
    exit(0)



