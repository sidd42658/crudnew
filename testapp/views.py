from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm

# Create your views here.
def welcome(request):
    emp=Employee.objects.all()
    return render(request,'testapp/crud.html',{'employee':emp})

def insert_emp_info(request):
    emp=Employee(name=request.POST['ename'],
                 salery=request.POST['esal'],
                 addr=request.POST['eaddr'],
                 desg=request.POST['edesg'])
    emp.save()
    return redirect('http://127.0.0.1:8000/')
def delete_employee(request,eid):
    emp=Employee.objects.get(id=eid)
    emp.delete()
    return redirect('http://127.0.0.1:8000/')


def update_view(request, id):
    emp = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        form.save()
        return redirect('http://127.0.0.1:8000/')

    return render(request, 'testapp/update.html', {'emp': emp})

