__author__ = 'mdu'
from pymongo import MongoClient
import datetime
try:
    from lxml import etree
except ImportError:
    print("lxml import error")
    raise
from datetime import datetime

def get_model_element_(elem):
    modelElement=[]
#*****************************
    modelElement.append(dict(parent_object=""))
    modelElement.append(dict(revision=""))
    modelElement.append(dict(model_revision=""))
    modelElement.append(dict(description=""))
    modelElement.append(dict(native_id=""))
    modelElement.append(dict(creation_date=datetime.now()))
    modelElement.append(dict(change_date=datetime.now()))
    modelElement.append(dict(archive="false"))
    modelElement.append(dict(deletede="false"))
#***************************************************

    modelElement.append(dict(name=next(iter(elem.xpath("./@ElementName")),"")))
    modelElement.append(dict(id=next(iter(elem.xpath("./@ElementId")),"")))
    modelElement.append(dict(type=next(iter(elem.xpath("./@TypeID")),"")))
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
            record=[]
            for recordFieldElement in recordElement.xpath("./www.qpr.com:Field",namespaces={'www.qpr.com': 'www.qpr.com'}):
                recordFieldName=next(iter(recordFieldElement.xpath("./@Name")),"")
                recordFieldValue=next(iter(recordFieldElement.xpath("./@Value")),"")
                recordField={}
                recordField[recordFieldName]=recordFieldValue
                record.append(recordField)
            records.append(record)
        if len(records):
            field_values_array.append(dict(Record=records))
        field[fieldName]=field_values_array
        data_section_2.append(field)
    modelElement.append(dict(data_section_2=data_section_2))
    return modelElement

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
            record=[]
            for recordFieldElement in recordElement.xpath("./www.qpr.com:Field",namespaces={'www.qpr.com': 'www.qpr.com'}):
                recordFieldName=next(iter(recordFieldElement.xpath("./@Name")),"")
                recordFieldValue=next(iter(recordFieldElement.xpath("./@Value")),"")
                recordField={}
                recordField[recordFieldName]=recordFieldValue
                record.append(recordField)
            records.append(record)
        if len(records):
            field_values_array.append(dict(Record=records))
        field[fieldName]=field_values_array
        data_section_2.append(field)
    modelElement["data_section_2"]=data_section_2
    return modelElement
client = MongoClient()
db=client.modelDB
model = db.model
# result=coll.insert_one({"x":"y"})
# #print(client.server_info())
# print(client.database_names())
# client.close()

#input_file='C:\\IdeaProjects\\hh_api_test\\MongoTest\\exp_types_formatted_few_elements.xml'
input_file='exp_types_formatted_few_elements.xml'
#input_file='C:\\Users\mdu\\Documents\\qpr_export\\exp.xml'
events = ("start", "end")
context = etree.iterparse(input_file,events = events, tag=('{www.qpr.com}ModelElement'))
count=0
for action, elem in context:
    if action=="end":
        #get_model_element(elem)
        #print(get_model_element(elem))
        modelElement=get_model_element(elem)
        model.insert(modelElement)
        print (modelElement["name"])
        count+=1
        elem.clear()
    while elem.getprevious() is not None:
        del elem.getparent()[0]
    # if count>1000:
        #     break
del context
print(count)
exit(0)


