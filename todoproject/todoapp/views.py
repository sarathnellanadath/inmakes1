from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from . forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class task_listview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'tasks'
class task_detailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'tasks'
class task_updateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'tasks'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})
class task_deleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('cbvhome')
















def add(request):
    tsk1 = task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority = request.POST.get('priority','')
        date=request.POST.get('date','')
        tsk=task(name=name,priority=priority,date=date)
        tsk.save()
    return render(request,'home.html',{'tasks':tsk1})
def delete(request,taskid):
    tsk=task.objects.get(id=taskid)
    if request.method == "POST":
        tsk.delete()
        return redirect('/')
    return render(request,'delete.html',{'tasks':tsk})
def update(request,taskid):
    tsk=task.objects.get(id=taskid)
    f=todoform(request.POST or None, instance=tsk)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html',{'f':f,'tasks':tsk})