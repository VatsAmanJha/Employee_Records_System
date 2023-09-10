from django.shortcuts import render, HttpResponse, redirect
from app import urls
from .models import Employee

# Create your views here.


def index(request):
    emp = Employee.objects.all()
    return render(request, "index.html", {"emp": emp})


def add_employee(request):
    if request.method == "POST":
        print("Data is Comming")
        name = request.POST.get("name")
        empid = request.POST.get("empid")
        email = request.POST.get("email")
        address = request.POST.get("address")
        mobile = request.POST.get("mobile")
        position = request.POST.get("position")
        department = request.POST.get("department")

        emp = Employee()
        emp.name = name
        emp.empid = empid
        emp.email = email
        emp.address = address
        emp.mobile = mobile
        emp.position = position
        emp.department = department
        emp.save()
        print("Data is Added")
        return redirect("home")
    return render(request, "add_employee.html", {})


def delete_emp(request, empid):
    print(empid)
    emp = Employee.objects.get(pk=empid)
    emp.delete()
    print("Data is Deleted")
    return redirect("home")


def update_employee(request, empid):
    print(empid)
    emp = Employee.objects.get(pk=empid)
    return render(request, "update_employee.html", {"emp": emp})


def do_update(request, empid):
    if request.method == "POST":
        name = request.POST.get("name")
        empid_temp = request.POST.get("empid")
        email = request.POST.get("email")
        address = request.POST.get("address")
        mobile = request.POST.get("mobile")
        position = request.POST.get("position")
        department = request.POST.get("department")

        emp = Employee.objects.get(pk=empid)

        emp.name = name
        emp.empid = empid_temp
        emp.email = email
        emp.address = address
        emp.mobile = mobile
        emp.position = position
        emp.department = department
        emp.save()
        print("Data Updated")
        return redirect("home")
