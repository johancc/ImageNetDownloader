"""
Takes in a dictionary of class names and returns the class ids
"""
import json 
class_info_json_filename = 'imagenet_class_info.json'

class_info_dict = dict()

limit = 1000

with open(class_info_json_filename) as class_info_json_f:
    class_info_dict = json.load(class_info_json_f)


def get_list_ids(class_name_filepath,start:int = 0, end:int = None, limit: int = None):
    class_name_dict = {}
    with open(class_name_filepath) as class_name_f:
        class_name_dict = json.load(class_name_f)
    if limit is None:
        limit = len(class_name_dict)
    if end is None:
        end = limit
    out = []
    errors = 0
    t = 0
    for name in class_name_dict.values():
        t+=1
        _id = name_to_id(name)
        if _id is None:
            errors += 1
        else:
            out.append(name_to_id(name))
    print("Finished with ", errors, " errors")
    

    return out[start:min([end,limit])]


def name_to_id(name):
    if "," in name:
        diambiguations = name.split(",")
    else:
        diambiguations = [name]
    for _id, val in class_info_dict.items():
        for word in diambiguations:
            if word in val.get("class_name"):
                return _id


if __name__ == "__main__":
    print(len(get_list_ids("index_to_name.json")))
    print(get_list_ids("index_to_name.json"))