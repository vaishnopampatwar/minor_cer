from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from home.models import CustomUser, Staff, Courses, Hod
# from .forms import AddStudentForm, EditStudentForm


def admin_home(request):
    return render(request,"admin_template/home_content.html")

def staff_add(request):
    courses=Courses.objects.all()
    return render(request,"admin_template/add_staff_template.html",{"courses":courses})

def staff_add_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('staff_add')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # course = request.POST.get('course')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            # user.staff.course = course
            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('staff_add/')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('staff_add/')

# def hod_home(request):
#     return render(request,"hod_template/hod_home_template.html")

def add_hod(request):
    return render(request,"admin_template/add_hod_template.html")

def add_hod_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_hod')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
            user.save()
            messages.success(request, "HoD Added Successfully!")
            return redirect('add_hod/')
        except:
            messages.error(request, "Failed to Add Hod!")
            return redirect('add_hod/')


def manage_hod(request):
    hod = Hod.objects.all()
    context = {
        "hod": hod
    }
    return render(request, "admin_template/manage_hod_template.html", context)

def delete_hod(request, hod_id):
    hod = Hod.objects.get(admin=hod_id)
    try:
        hod.delete()
        messages.success(request, "HoD Deleted Successfully.")
        return redirect('manage_hod')
    except:
        messages.error(request, "Failed to Delete Staff.")
        return redirect('manage_hod')

def manage_staff(request):
    staff = Staff.objects.all()
    context = {
        "staff": staff
    }
    return render(request, "admin_template/manage_staff_template.html", context)

def delete_staff(request, staff_id):
    staff = Staff.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request, "Staff Deleted Successfully.")
        return redirect('manage_staff')
    except:
        messages.error(request, "Failed to Delete Staff.")
        return redirect('manage_staff')


def add_course(request):
    staff = CustomUser.objects.filter(user_type='2')
    context = {
        "staff": staff
    }
    return render(request, "admin_template/add_course_template.html",context)

def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_course')
    else:
        cn = request.POST.get('cname')
        cc = request.POST.get('code')
        sem = request.POST.get('sem')
        ay = request.POST.get('ay')
        minor = request.POST.get('minor')
        
        stf=request.POST.get('staff')
        staff = CustomUser.objects.get(id=stf)

        cred = request.POST.get('cred')
        try:
            course_model = Courses(course_code=cc,course_name=cn,sem=sem,academic_year=ay,minor=minor,credits=cred,staff_id=staff)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('add_course')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('add_course')


def manage_course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'admin_template/manage_course_template.html', context)

def delete_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    try:
        course.delete()
        messages.success(request, "Course Deleted Successfully.")
        return redirect('manage_course')
    except:
        messages.error(request, "Failed to Delete Course.")
        return redirect('manage_course')