from django.urls import path
from hrmapp.views import *

urlpatterns = [
    path('hrm/',hrm , name='hello'),
]
