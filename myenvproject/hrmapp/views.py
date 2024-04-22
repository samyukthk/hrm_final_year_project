from django.shortcuts import render
from myenvapp.views import *
# Create your views here.
@api_view()
def hrm(request):
    return Response({"message": "this is may hrm app!"})
    