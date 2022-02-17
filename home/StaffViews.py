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

def staff_home(request):
    courses = Courses.objects.all()
    staff = CustomUser.objects.filter(user_type='2')
    context = {
        "courses": courses,
        "staff": staff
    }
    return render(request, "staff_template/staff_home_template.html",context)

def add_student(request):
    courses = Courses.objects.all()
    staff = CustomUser.objects.filter(user_type='2')
    context = {
        "courses": courses,
        "staff": staff
    }
    return render(request, 'staff_template/add_student_template.html',context)

def add_student_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_student')
    else:
        prn = request.POST.get('prn')
        name = request.POST.get('name')
        mname = request.POST.get('mname')
        password = request.POST.get('password')
        mob = request.POST.get('mob')
        email = request.POST.get('email')
        sas = request.POST.get('sas')
        cor_n = request.POST.get('courses')
        cid = Courses.objects.get(id=cor_n)

        date = request.POST.get('date')
        time = request.POST.get('time')
        
        # course = request.POST.get('course')
        try:
            student_model = Student(prn=prn, name=name, mother_name=mname, password=password, 
            mob=mob, email=email,sas=sas,course_id=cid,date=date,time=time)
            # user.staff.course = course 
            student_model.save()
            messages.success(request, "Student Added Successfully!")
            return redirect('add_student')
        except Exception as e:
            messages.error(request, "Failed to Add Student!")
            return redirect('add_student')

def manage_student(request):
    student = Student.objects.all()
    context = {
        "student": student
    }
    return render(request, 'staff_template/manage_student_template.html', context)

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    try:
        student.delete()
        messages.success(request, "Student Deleted Successfully.")
        return redirect('manage_student')
    except:
        messages.error(request, "Failed to Delete Student.")
        return redirect('manage_student')

def show_student(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_student')
    else:
        course=request.POST.get('course')
        course = Courses.objects.get(id=course)

        student=Student.objects.all()
        context = {
        "course": course,
        "student":student
        }
        return render(request, 'staff_template/manage_student_template.html',context)


def result_home(request):
    return render(request, 'staff_template/result_home_template.html')

def add_result(request):
    courses = Courses.objects.all()
    staff = CustomUser.objects.filter(user_type='2')
    context = {
        "courses": courses,
        "staff": staff
    }
    return render(request, 'staff_template/add_stud_result_template.html',context)

def add_result_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_result')
    else:
        prn = request.POST.get('prn')
        name = request.POST.get('name')
        course_name= request.POST.get('course_name')
        grade = request.POST.get('grade')
 
        try:
            result_model = StudentResult(prn=prn,name=name,course_name=course_name,grade=grade)
            result_model.save()
            messages.success(request, "Result Added Successfully!")
            return redirect('add_result')
        except Exception as e:
            messages.error(request, "Failed to Add Result!")
            return HTTPResponse(type(e))

def manage_result(request):
    result = StudentResult.objects.all()
    context = {
        "result": result    
    }
    return render(request, 'staff_template/result_home_template.html', context)

def delete_result(request, result_id):
    result = StudentResult.objects.get(id=result_id)
    try:
        result.delete()
        messages.success(request, "Student Deleted Successfully.")
        return redirect('manage_result')
    except:
        messages.error(request, "Failed to Delete Student.")
        return redirect('manage_result')



def resultana_home(request):
    return render(request, 'staff_template/resultana_home_template.html')

def add_ana(request):
    courses = Courses.objects.all()
    staff = CustomUser.objects.filter(user_type='2')
    context = {
        "courses": courses,
        "staff": staff
    }
    return render(request, 'staff_template/add_stud_resultana_template.html',context)

def add_resultana_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_ana')
    else:
        res = ResultAnalysis()
        name = request.POST.get('course')
        res.course_id = Courses.objects.get(id=name)

        if len(request.FILES) != 0:
            res.result_file = request.FILES['file']

        # name = request.POST.get('course')
        # cid = Courses.objects.get(id=name)
        # file = request.POST.get('file')
        try:
            # result_model = ResultAnalysis(course_id=cid,result_file=file)
            res.save()
            messages.success(request, "Result Added Successfully!")
            return redirect('add_result')
        except Exception as e:
            messages.error(request, "Failed to Add Result!")
            return HttpResponse(e)

def man_resultana(request):
    result = ResultAnalysis.objects.all()
    context = {
        "result": result
    }
    return render(request, 'staff_template/resultana_home_template.html', context)

def del_resultana(request, result_id):
    res = ResultAnalysis.objects.get(id=result_id)
    try:
        res.delete()
        messages.success(request, "Result Analysis Deleted Successfully.")
        return redirect('man_resultana')
    except:
        messages.error(request, "Failed to Delete Result Analysis.")
        return redirect('man_resultana')


def showfile(request):

    lastfile= ResultAnalysis.objects.last()

    filepath= lastfile.filepath

    filename= lastfile.name


    form= FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'filepath': filepath,
              'form': form,
              'filename': filename
              }
    
      
    return render(request, 'staff_template/result_home_template.html', context)