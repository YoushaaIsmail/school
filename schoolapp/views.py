from django.shortcuts import render
from .models import Class
from .utilities import get_School

def our_School(request):
    school1=get_School(request)
    classes=Class.objects.filter(school=school1)
    return render(request ,'School/our_School.html',{'school':school1,'class':classes})

