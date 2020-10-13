from django.shortcuts import render,redirect
from .models import View
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    if request.method=='POST':
        name=request.POST['name']
        branch=request.POST['branch']
        age=request.POST['age']
        add_data=View(name=name,branch=branch,age=age)
        add_data.save()
        messages.info(request,'Added Successfully')
        return redirect("/")
    else:
        return render(request,'index.html')

def fetch(request):
    data=View.objects.all
    return render(request,"fetch.html",{"data":data})
def edit(request,id):
    edit_data=View.objects.get(id=id)
    return render(request,"edit.html",{"edit_data":edit_data})

def delete(request,id):
    delete_data=View.objects.get(id=id)
    delete_data.delete()
    return redirect('/fetch')

def update(request):
    id=request.POST['id']
    name=request.POST['name']
    branch=request.POST['branch']
    age=request.POST['age']
    update_data=View(id=id,name=name,branch=branch,age=age)
    update_data.save()
    return redirect("/fetch")
