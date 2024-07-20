from django.shortcuts import render,redirect

from . models import *
from .forms import *
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.
def home(request):
    catagory=Catagory.objects.filter(status=0)

    return render(request, "index.html", {"catagory": catagory})
    

def doctors_view(request,type):
    if True:
        doctors=Doctors.objects.filter(category__type=type)
        return render(request,"doctors.html",{"doctors":doctors,"category_type":type})
    else:
        return redirect('Home')
     
def get_variable():    
    my_variable = "Hello from file1!"
    return my_variable

n=[0]
def create_profile(request,name):
     
     if request.method == 'POST':
        name1 = request.POST.get('name')
        fh = request.POST.get('fh')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        description = request.POST.get('description')
        gender = request.POST.get('gender')
        #datetime_field_str = request.POST.get('datetime_field')

        # Convert datetime string to datetime object
    
        n1=n[0]+1
        n[0]=n1
        UserProfile.objects.create(
            pid='ID00'+str(n1),
            doctor=name,
            name=name1,
            fh=fh,
            age=age,
            contact=contact,
            description=description,
            gender=gender,
            #datetime_field=datetime_field
        )
        return redirect('msg')  # Redirect to a success page or another view
     
     return render(request, 'register.html', {'name':name})


def doc_profile(request):
    if request.method=='POST':
        d_name = request.POST.get('name')
        psw = request.POST.get('password')
        if(Doctors.objects.filter(name=d_name,password=psw)):
            
            response = redirect('P_details', d_name)
    
            response.set_cookie('Doctor', d_name)
            return response
        
        else:
            messages.warning(request, 'Wrong UserID and Password')
            return render(request,"doc_profile.html")

    return render(request,"doc_profile.html")

def p_details(request,p_name):
    if request.method == 'POST':
        # Retrieve form data
        doc = request.POST.get('doctor')
        name1 = request.POST.get('name')
        fh = request.POST.get('fh')
        next_date = request.POST.get('date')
        description = request.POST.get('des')
        prescription1 = request.POST.get('prs')
        
        prescription.objects.create(
            doctor=doc,
            name=name1,
            fh=fh,
            nadate=next_date,
            description=description,
            prc=prescription1,
        )
        
    patient=UserProfile.objects.filter(doctor=p_name)
    return render(request,"p_details.html", {'patients':patient})


def all_patient(request):
    
    patient=prescription.objects.all()
   
    return render(request,"all_patient.html", {'patients':patient})

def prescription1(request,id):
    if request.method=='post':
        doctor = request.POST['doctor']
        name = request.POST['name']
        fh = request.POST['fh']
        date = request.POST['date']
        des = request.POST['des']
        prs = request.POST['prs']
        pro = prescription(
            doctor=doctor,
            name=name,
            fh=fh,
            nadate=date,
            description=des,
            prc=prs,
            #datetime_field=datetime_field
        )
        pro.save()
        return redirect('doc_profile')
    patient=UserProfile.objects.filter(id=id)
    return render(request,"prescription.html",{'patient':patient})

def msg(request):
    return render(request,"msg.html")

