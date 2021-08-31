from django.shortcuts import render

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
import math
from django.http import HttpResponse
from rest_framework import status
import logging
logging.basicConfig(filename='basiclogs.log', encoding='utf-8', level=logging.INFO)
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

@api_view(['POST','GET'])
@permission_classes ([AllowAny,])
@csrf_exempt
def find_sum(request):
    a = request.data.get('a')
    b = request.data.get('b')
    c = int(a)+int(b)
    logging.info("-------------------")
    logging.info(request.data)
    logging.info(request.META)



    logging.info("===================")



    return Response({"c":c})

@api_view(['POST','GET'])
@csrf_exempt
def makelogs(request):

    logging.warning('is when this event was logged.')
    return HttpResponse('logfile',status=status.HTTP_200_OK)