from django.shortcuts import render,redirect
from .models import Course
from .forms import CourseForm

# Create your views here.
def home(request):
 all = Course.objects.all()
 return render (request,'day4/home.html',{'all_courses':all})

def remove(request, id):
 c=Course.objects.get(id=id)
 c.delete()
 return redirect(home)

def edit(request, id):
 c=Course.objects.get(id=id)
 frm=CourseForm(instance=c)
 if request.method=='POST':
  frm = CourseForm(request.POST,instance=c)
  if frm.is_valid():
    frm.save()
  return redirect(home)


  
 return render(request,'day4/edit.html',{'form':frm})

def add(request):
 frm = CourseForm()

 return render (request,'day4/add.html',{'form':frm})

def save(request):
 if(request.method=='POST'):
  frm = CourseForm(request.POST)
  frm.save()
  return redirect (home)
 return redirect (home)

