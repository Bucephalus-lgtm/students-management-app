from django.shortcuts import render, redirect
from .forms import studentForm
from .models import student

# Create your views here.


def student_list(request):
    context = {'student_list': student.objects.all()}
    return render(request, "student_register/student_list.html", context)


def student_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = studentForm()
        else:
            student = student.objects.get(pk=id)
            form = studentForm(instance=student)
        return render(request, "student_register/student_form.html", {'form': form})
    else:
        if id == 0:
            form = studentForm(request.POST)
        else:
            student = student.objects.get(pk=id)
            form = studentForm(request.POST,instance= student)
        if form.is_valid():
            form.save()
        return redirect('/student/list')


def student_delete(request,id):
    student = student.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')
