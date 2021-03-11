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
    data = request.data
    support_multiple = validators.string_to_bool(data.get("support_multiple","false"))
    pick_first = validators.string_to_bool(data.get("pick_first","false"))


    result = validators.validate_finite_values_entity(
        json.loads(data.get("values")),
        json.loads(data.get("supported_values")),
        data.get("invalid_trigger"),
        data.get("key"),
        support_multiple,
        pick_first
    )
    
    return JsonResponse(result)
    

@api_view(['POST'])
def validate_numeric_api(request):
    data = request.data
    support_multiple = validators.string_to_bool(data.get("support_multiple","false"))
    pick_first = validators.string_to_bool(data.get("pick_first","false"))
    
    result=validators.validate_numeric_entity(
        json.loads(data.get("values")),
        data.get("invalid_trigger"),
        data.get("key"),
        support_multiple,
        pick_first,
        data.get("constraint"),
        data.get("var_name")
    )

    
    return JsonResponse(result)




