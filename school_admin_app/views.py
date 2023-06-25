from django.shortcuts import render,HttpResponse,redirect
from school_admin_app.models import *

# Create your views here.

def login(request):
    return render(request,'login.html')

def admin_home(request):

    if 'j' in request.GET:
        jump=request.GET
        if jump['j'] == '3' :
            return render(request,'unit.html',{
                'units':Unit.objects.filter(subject_ID=Subject.objects.get(id=jump['ro'])),
                'model_name':Subject.objects.get(id=jump['ro']),
                'classes':Class.objects.all(),
                'subjects':Subject.objects.all()
            })
        if jump['j'] == '3' :
            return render(request,'course.html',{
                'units':Unit.objects.filter(subject_ID=Subject.objects.get(id=jump['ro'])),
                'model_name':Subject.objects.get(id=jump['ro']),
                'classes':Class.objects.all(),
                'subjects':Subject.objects.all()
    })




    return render(request,'Scchools.html',{
        'schools':School.objects.all(),
        'classes':Class.objects.all(),
        'subjects':Subject.objects.all()
    })

def add_school(request):
    if request.method == 'POST':

        new_school=School()
        new_school.name=str(request.POST['name'])
        new_school.admin_name=str(request.POST['admin'])
        new_school.email=str(request.POST['email'])
        new_school.password=str(request.POST['password'])
        new_school.address=str(request.POST['address'])
        new_school.phone_number=int(request.POST['phone'])
        new_school.save()
        return redirect('admin_home')
    schools=School.objects.all()
    return render(request,'Addschool.html',{
    })





