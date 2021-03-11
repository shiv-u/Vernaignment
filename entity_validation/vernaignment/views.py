from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import validators
import json



# Create your views here.


@api_view(['POST'])
def validate_finite_values_api(request):
    # return validators.validate_finite_values_entity(request.data)
    pass
    

@api_view(['POST'])
def validate_numeric_api(request):
    data = request.data
    
    result=validators.validate_numeric_entity(
        json.loads(data.get("values")),
        data.get("invalid_trigger"),
        data.get("key"),
        bool(data.get("support_multiple",False)),
        bool(data.get("pick_first",False)),
        data.get("constraint"),
        data.get("var_name")
    )

    response_data={}
    response_data["filled"]=result[0]
    response_data["partially_filled"]=result[1]
    response_data["trigger"]=result[2]
    response_data["parameters"]=result[-1]
    
    return JsonResponse(response_data)




