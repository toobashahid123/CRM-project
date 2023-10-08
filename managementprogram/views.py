
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import Member
import os

# Create your views here.



def index(request):
     if 'q' in request.GET:
         q = request.GET['q']
         emps = Member.objects.filter(Name__icontains = q )
     else:
         emps = Member.objects.all()
     context={'emps':emps}
     return render(request, 'index.html',context)

def add_emp(request):
    if request.method == "POST":
        Name=request.POST['Name']
        city=request.POST['city']
        Title=request.POST['Title']
        emailid=request.POST['emailid']
        salary=request.POST['salary']
        last_name=request.POST['last_name']
        new_emp=Member(Name=Name, city=city, Title=Title, emailid=emailid, last_name=last_name, salary=salary)
        new_emp.save()
        messages.success(request, "Profile added succussfully!")
        return redirect('index')
    elif request.method == "GET":
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("Exceptional Error occured!")
    
def customer_record(request, pk):
     #if request user.is_authenticated:
     customer_record= Member.objects.get(id=pk)
     return render(request, 'record.html', {'customer_record':customer_record})

def delete_record(request, pk):
     #if request user.is_authenticated:
     delete_record= Member.objects.get(id=pk)
     delete_record.delete()
     messages.success(request, "Profile delete succussfully.")
     return redirect('index')

def edit_record(request, pk):
     prod = Member.objects.get(id=pk)
     if request.method == "POST":
        if len(request.FILES) != 0:
             if len(prod.Name)>0:
                  os.remove(prod.Name.path)
                  prod.Name = request.FILES['prod.Name']
             prod.city=request.POST['prod.city']
             prod.Title=request.POST['prod.Title']
             prod.emailid=request.POST['prod.emailid']
             prod.salary=request.POST['prod.salary']
             prod.last_name=request.POST['prod.last_name']#prod=Member(Name=Name, city=city, Title=Title, emailid=emailid, last_name=last_name, salary=salary)
             prod.save()
             messages.success(request, "Profile Edit succussfully!")
             return redirect('index')
     context = {'prod': prod}
     return render(request, 'edit.html',context)



          
    
          


      


               

    
    








    