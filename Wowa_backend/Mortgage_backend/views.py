from django.shortcuts import render
from rest_framework.utils import json

from .models import Mortgage_values
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializers import Mortgage_Data_Serializer


@api_view(['GET'])
def api_overview(request):
    return Response('Hello')


@api_view(['Get'])
def get_mortgage_data(request):
    data = Mortgage_values.objects.all()
    serializer = Mortgage_Data_Serializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def insert_json_data(request):
    data = json.load(request.data.get("File"))
    for value in data:
        serializer = Mortgage_Data_Serializer(data=value)
        if serializer.is_valid():
            serializer.save()
    return Response("200")
