from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def homeView(request):
    return render(request,'index.html')


from django.views.generic import ListView
from StudentRegistry.models import StudentData

class StudentReport(ListView):
    model = StudentData

from django.views.generic import CreateView,UpdateView,DeleteView

class AddStudent(CreateView):
    model = StudentData
    fields = ['id','firstName','lastName','standard','fatherName','fatherContact']

class UpdateStudent(UpdateView):
    model = StudentData
    fields = ['firstName','lastName','standard','fatherName','fatherContact']
    template_name = "StudentRegistry\studentdata_update_form.html"

    success_url = '/'

class RemoveStudent(DeleteView):
    model = StudentData
    success_url = '/'