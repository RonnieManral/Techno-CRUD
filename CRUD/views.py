from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from CRUD.forms import EmployeeForm
from .forms import EmployeeForm
from datetime import datetime

from CRUD.models import Employee

# Create your views here.
def employee_list(request):
    employees=Employee.objects.all()
    return render(request,'employee_list.html',{'employees':employees})

def add(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        add=Employee(username=username,firstname=firstname,lastname=lastname,email=email,created=datetime.today())
        add.save()

    latest_by=[Employee.objects.latest('created')]
    param={'latest_by':latest_by}
    return render(request,'add.html',param)

def edit(request,id):
    employee=Employee.objects.filter(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee=Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None,instance = employee)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})

def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/")

def get(request):
    query=request.GET['query']
    param=Employee.objects.filter(id=query)
    context={'param':param}
    return render(request,"get.html",context)

