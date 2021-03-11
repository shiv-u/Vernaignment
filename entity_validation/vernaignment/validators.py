from typing import List, Dict, Callable, Tuple
from django.http import HttpResponse


SlotValidationResult = Tuple[bool, bool, str, Dict]

def build_response(result):
    response_data={}
    response_data["filled"]=result[0]
    response_data["partially_filled"]=result[1]
    response_data["trigger"]=result[2]
    response_data["parameters"]=result[3]

    return response_data


def string_to_bool(bool_string):
    s_dict = {"true":True,"false":False}
    return s_dict[bool_string]


def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None,
                                invalid_trigger: str = None, key: str = None,
                                support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:
    """
    Validate an entity on the basis of its value extracted.
    The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").

    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param supported_values: List of supported values for the slot
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :return: a tuple of (filled, partially_filled, trigger, params)
    """

    values_length = len(values)
    filled_count = 0
    filled=False
    partially_filled=False
    trigger=""

    params={key:[]}
    
  

    if values_length==0:
        return (False,False,trigger,{})
    

    for doc in values:
        print(params,pick_first)
        try:
            if supported_values.index(doc["value"]) >= 0:
                filled_count+=1
                params[key].append(doc["value"])
        except:
            trigger = invalid_trigger
        
    
    if filled_count==values_length:
        filled = True
        partially_filled = False
    else:
        partially_filled=True

    
    if len(params[key])==0:
        params={}
    elif pick_first and len(params[key])>0:
        params[key]=params[key][0]
    
    response = (filled,partially_filled,trigger,params)
    
    return build_response(response)

        
    



def validate_numeric_entity(values: List[Dict], invalid_trigger: str = None, key: str = None,
                            support_multiple: bool = True, pick_first: bool = False, constraint=None, var_name=None,
                            **kwargs) -> SlotValidationResult:
    """
    Validate an entity on the basis of its value extracted.
    The method will check if that value satisfies the numeric constraints put on it.
    If there are no numeric constraints, it will simply assume the value is valid.

    If there are numeric constraints, then it will only consider a value valid if it satisfies the numeric constraints.
    In case of multiple values being extracted and the support_multiple flag being set to true, the extracted values
    will be filtered so that only those values are used to fill the slot which satisfy the numeric constraint.

    If multiple values are supported and even 1 value does not satisfy the numeric constraint, the slot is assumed to be
    partially filled.

    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :param constraint: Conditional expression for constraints on the numeric values extracted
    :param var_name: Name of the var used to express the numeric constraint
    :return: a tuple of (filled, partially_filled, trigger, params)
    """
   
    values_length = len(values)
    count = 0
    filled=False
    partially_filled=False
    trigger=""

    params={key:[]}
  

    if values_length==0:
        return (False,False,trigger,{})
    

    for doc in values:
        print(params)

        exp = constraint.replace(var_name,str(doc["value"]))
        result = eval(exp)

        if result:
            count+=1
            params[key].append(doc["value"])
            
        else:
            trigger=invalid_trigger
            
            
    
    if count==values_length:
        filled = True
        partially_filled = False
    else:
        partially_filled=True

    
    if len(params[key])==0:
        params={}
    elif pick_first and len(params[key])>0:
        params[key]=params[key][0]
    
    response = (filled,partially_filled,trigger,params)
    
    return build_response(response)

        


