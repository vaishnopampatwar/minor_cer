from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .forms import FileForm
from home.models import CustomUser, Staff, Courses,Student,StudentResult,ResultAnalysis
import mysql.connector
mydb = mysql.connector.connect(
        user="ux5kocwc97eprzzo",
        password="YIxg2EmwcBBuEdB4iGS1",
        database="bnsbdby2zxhx9g5dnhpe",
        host="bnsbdby2zxhx9g5dnhpe-mysql.services.clever-cloud.com",
)
def hod_home(request):
    #print("outside block")
    if request.method == "POST":
        prn = request.POST.get("prn")
        mycursor=mydb.cursor()
        query="select prn,name,grade,course_name from home_studentresult where prn='{0}';".format(prn)
        mycursor.execute(query)
        stuInfo=mycursor.fetchall()
        print(stuInfo)

        data={
        'stuInfo':stuInfo
        }
        return render(request,"hod_template/manage_result_template.html",data)
    return render(request,"hod_template/hod_home_template.html")

