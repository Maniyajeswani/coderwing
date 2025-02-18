from django.shortcuts import render,get_object_or_404,redirect
from .models import Employees
from django.contrib import messages
from django.db.models import Q



# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employees.objects.all()
    context={
        'emps':emps
    }
    return render(request,'all_employee.html',context)

def add_emp(request):
    return render(request,'add_employee.html')

def submit(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        role=request.POST['role']
        phone=request.POST['phone']
        hire_date=request.POST['hire_date']
       
        existing_employee = Employees.objects.filter(
            first_name=first_name,
            last_name=last_name,
            phone=phone
        ).exists()
        if existing_employee:
            messages.error(request,"Already exists")
            return render(request,'add_employee.html')
        else:
            Employees.objects.create(first_name=first_name,last_name=last_name,dept=dept,salary=salary,bonus=bonus,role=role,phone=phone,hire_date=hire_date)
            emps=Employees.objects.all()
            context={
            'emps':emps
            }
            return render(request,'all_employee.html',context)

        
    else:
        return render(request,'add_employee.html')

from django.shortcuts import redirect
from .models import Employees
from django.contrib import messages

def remove_emp(request, emp_id=None):
    if emp_id:
        try:
            emp_to_be_removed = Employees.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            messages.success(request, "Employee removed successfully!")
            
        except Employees.DoesNotExist:
            messages.error(request, "Employee not found!")
    
    # Fetch the updated list of employees
    emps = Employees.objects.all()

    # Pass the updated list to the template
    context = {
        'emps': emps
    }
    return render(request, 'remove_employee.html', context)


def promote_employee(request, employee_id=0):
    if employee_id:  # If an employee is selected, show the promotion form
        employee = get_object_or_404(Employees, id=employee_id)

        if request.method == "POST":
            new_position = request.POST.get('new_position')  
            new_salary = request.POST.get('new_salary')  

            if new_position:
                employee.role = new_position
            if new_salary:
                employee.salary = new_salary  
            
            employee.save()
            messages.success(request, f"{employee.first_name} has been promoted to {new_position}.")
            return redirect('all_emp')  # Redirect back to the selection page

        return render(request, 'promote_employee.html', {'employee': employee})

    # If no employee_id, show dropdown menu to select employee
    employees = Employees.objects.all()
    return render(request, 'select_employee.html', {'employees': employees})
