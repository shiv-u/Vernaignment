from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import validators



# Create your views here.


@api_view(['POST'])
def validate_finite_values_api(request):
    # return validators.validate_finite_values_entity(request.data)
    pass
    

@api_view(['POST'])
def validate_numeric_api(request):
    # return validators.validate_numeric_entity(request.data)
    pass




