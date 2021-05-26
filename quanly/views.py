from typing import ContextManager
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, EmpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee


# Create your views here.
def login_page(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'User or password incorrect')
     
    return render(request, 'quanly/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')


def register_page(request):

    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        # else:
        #     messages.error(request, 'Account created unsuccessfully')

    context = {'form':form,
                
    }

    return render(request,'quanly/register.html', context)

@login_required(login_url='login')
def dashboard(request):

    emp = Employee.objects.all()
    

    context = {'emps':emp}
    return render(request, 'quanly/Staff.html', context)

@login_required(login_url='login')
def add_emp(request):
    form = EmpForm()
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request, 'quanly/emp_form.html',context)
    

@login_required(login_url='login')
def update_emp(request, id):
    emp = Employee.objects.get(id=id)
    form = EmpForm(instance=emp)
    if request.method == "POST":
        form = EmpForm(request.POST, instance=emp)
        if form.is_valid:
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'quanly/emp_form.html',context)


@login_required(login_url='login')
def delete_emp(request, id):
    emp = Employee.objects.get(id=id)
    if request.method == "POST":
        emp.delete()
        return redirect ('dashboard')
    context =  {'nhanvien':emp}
    return render(request, 'quanly/delete_confirm.html',context)

@login_required(login_url='login')
def details_emp(request, id):
    emp = Employee.objects.get(id=id)
    form = EmpForm(instance=emp)
    if request.method == "POST":
      
        return redirect ('dashboard')
    context = {'form': form}
    return render(request, 'quanly/details.html',context)    
    
