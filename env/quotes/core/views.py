from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.

from . eliza import Eliza 
  
class ReactView(APIView):
    
    serializer_class = ReactSerializer
  
    def get(self, request):
        detail = [ {"name": detail.name,"detail": detail.detail} 
        for detail in React.objects.all()]
        return Response(detail)
  
    def post(self, request):
  
        eliza = Eliza()
        answer = eliza.respond(request.data['name'])
        request.data['detail'] = answer
        serializer = ReactSerializer(data=request.data) 
        print("#" , request.data['name'] , request.data['detail'])
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data) 