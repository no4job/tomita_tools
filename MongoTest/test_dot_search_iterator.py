__author__ = 'mdu'
#{'native_id': '', 'description': '', 'archive': 'false', 'id': 'PG_FL11527526', 'creation_date': datetime.datetime(2016, 4, 30, 21, 18, 18, 194485), 'change_date': datetime.datetime(2016, 4, 30, 21, 18, 18, 194485), 'parent_object': '', 'model_revision': '', 'data_section_2': [{'Description': []}, {'Name translations': []}, {'Description translations': []}, {'ScoreCard model': []}, {'Scorecard identifier': []}, {'Measure identifier': []}, {'Multiplicity (Start)[Multiplicity]': []}, {'Multiplicity (Start)[Multiplicity].': []}, {'Multiplicity (Start)[Multiplicity]."0..1"': []}, {'Multiplicity (Start)[Multiplicity]."0..*"': []}, {'Multiplicity (Start)[Multiplicity].1': []}, {'Multiplicity (Start)[Multiplicity]."1..*"': []}, {'Multiplicity (End)[Multiplicity]': []}, {'Multiplicity (End)[Multiplicity].': []}, {'Multiplicity (End)[Multiplicity]."0..1"': []}, {'Multiplicity (End)[Multiplicity]."0..*"': []}, {'Multiplicity (End)[Multiplicity].1': []}, {'Multiplicity (End)[Multiplicity]."1..*"': []}, {'Information Items': []}, {'Resources': []}, {'Measure data': []}, {'Transfer Type': []}, {'From': [{'Record': [{'ElementId': 'PG_EL365325006', 'TypeName': 'Application Component', 'TypeID': 'PG_EL1536990702', 'ElementName': 'Модуль ОТТ Smart Tube SDP (КЦ)', 'InstanceId': '228763353', 'ElementSymbol': 'MO365325006'}]}]}, {'To': [{'Record': [{'ElementId': 'PG_EL1491507864', 'TypeName': 'Application Component', 'TypeID': 'PG_EL1536990702', 'ElementName': 'Smart Tube SDP (Урал)', 'InstanceId': '226387172', 'ElementSymbol': 'MO1491272444_1'}]}]}, {'Owner': []}, {'Information Item': []}, {'Information flow': [{'Value': ['false']}]}, {'Priority': [{'Value': ['0']}]}, {'Can be suspended': [{'Value': ['false']}]}, {'Processing time': [{'Value': ['Constant']}]}, {'Durations': [{'Value': ['0d 00:00:00']}]}, {'Activation Frequency': [{'Value': ['Constant']}]}, {'Intervals': [{'Value': ['0d 00:00:00']}]}, {'Start simulation': [{'Value': ['false']}]}, {'Number of activations': [{'Value': ['0']}]}, {'Interface element': [{'Value': ['false']}]}, {'Interface mappings': []}], 'name': '', 'deleted': 'false', 'type': 'PG_FL784142384'}
def remove_dots(data):
    if type(data)is dict:
        for key in data.keys():
            if type(data[key]) is dict:
                data[key] = remove_dots(data[key])
            elif type(data[key])is list:
                for item in data[key]:
                    remove_dots(item)
            if '.' in key:
                #data[key.replace('.', '\uff0E')] = data[key]
                data[key.replace('.', '#')] = data[key]
                del data[key]
    if type(data)is list:
        for item in data:
            remove_dots(item)
            #if item is dict: data[key] = remove_dots(data[key])
    return data

element={'native_id': '', 'description': '', 'archive': 'false', 'id': 'PG_FL11527526', 'parent_object': '', 'model_revision': '', 'data_section_2': [{'Description': []}, {'Name translations': []}, {'Description translations': []}, {'ScoreCard model': []}, {'Scorecard identifier': []}, {'Measure identifier': []}, {'Multiplicity (Start)[Multiplicity]': []}, {'Multiplicity (Start)[Multiplicity].': []}, {'Multiplicity (Start)[Multiplicity]."0..1"': []}, {'Multiplicity (Start)[Multiplicity]."0..*"': []}, {'Multiplicity (Start)[Multiplicity].1': []}, {'Multiplicity (Start)[Multiplicity]."1..*"': []}, {'Multiplicity (End)[Multiplicity]': []}, {'Multiplicity (End)[Multiplicity].': []}, {'Multiplicity (End)[Multiplicity]."0..1"': []}, {'Multiplicity (End)[Multiplicity]."0..*"': []}, {'Multiplicity (End)[Multiplicity].1': []}, {'Multiplicity (End)[Multiplicity]."1..*"': []}, {'Information Items': []}, {'Resources': []}, {'Measure data': []}, {'Transfer Type': []}, {'From': [{'Record': [{'ElementId': 'PG_EL365325006', 'TypeName': 'Application Component', 'TypeID': 'PG_EL1536990702', 'ElementName': 'Модуль ОТТ Smart Tube SDP (КЦ)', 'InstanceId': '228763353', 'ElementSymbol': 'MO365325006'}]}]}, {'To': [{'Record': [{'ElementId': 'PG_EL1491507864', 'TypeName': 'Application Component', 'TypeID': 'PG_EL1536990702', 'ElementName': 'Smart Tube SDP (Урал)', 'InstanceId': '226387172', 'ElementSymbol': 'MO1491272444_1'}]}]}, {'Owner': []}, {'Information Item': []}, {'Information flow': [{'Value': ['false']}]}, {'Priority': [{'Value': ['0']}]}, {'Can be suspended': [{'Value': ['false']}]}, {'Processing time': [{'Value': ['Constant']}]}, {'Durations': [{'Value': ['0d 00:00:00']}]}, {'Activation Frequency': [{'Value': ['Constant']}]}, {'Intervals': [{'Value': ['0d 00:00:00']}]}, {'Start simulation': [{'Value': ['false']}]}, {'Number of activations': [{'Value': ['0']}]}, {'Interface element': [{'Value': ['false']}]}, {'Interface mappings': []}], 'name': '', 'deleted': 'false', 'type': 'PG_FL784142384'}
remove_dots(element)
pass