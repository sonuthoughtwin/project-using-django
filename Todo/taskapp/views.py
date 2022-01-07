from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Task

# Create your views here.
def index(request):
    if request.method == 'POST':
            content = Task(task_title = request.POST["title"], task_content =request.POST["txtcontent"], created_date = request.POST["txtdate"])
            content.save()
            return render(request, "index.html", {"res":"task add successfully"})
    return render(request, "index.html")

def show_task(request):
    t = Task.objects.all() 
    return render(request,"showtask.html",{'key':t})

def find_task(request):
    findt = Task.objects.get(pk=int(request.GET["q"])) 
    return render(request,"findtask.html",{'res':findt})

def edit_task(request):
        edit = Task.objects.get(pk=int(request.POST['txtid']))   
        edit.task_title = request.POST["txttitle"]
        edit.task_content =request.POST["txtcontent"]
        edit.save()
        return redirect('show_task')

def delete_task(request, pk):
    s = Task.objects.get(id = pk)
    if request.method == 'POST':
        s.delete()
        return HttpResponseRedirect('/show_task')
    return render(request, "delete.html",{"res":s.task_title})
       	

    




