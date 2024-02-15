from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from  day4app.models import Course
from .forms import Student_Form
from .models import Student

# Create your views here.



def student_register(request):
    frm = Student_Form()
    all_courses = Course.objects.all()
    return render (request,'day5/add_student.html',{'form':frm ,'all_courses':all_courses })

def add_student(request):
 frm = Student_Form()
 return render (request,'day5/add_student.html',{'form':frm})

def save_student(request):
    if (request.method =='POST'):
        frm = Student_Form(request.POST)
        frm.save()
        return redirect(student_register)
    return redirect(student_register)

def remove_course(request, std_id, course_id):
    student = get_object_or_404(Student, std_id=std_id)
    course = get_object_or_404(student.std_enrolled_courses, id=course_id)
    student.std_enrolled_courses.remove(course)
    return render(request, 'day5/student_info.html', {'student': student})

def remove_student(request, std_id):
 stu=Student.objects.get(std_id=std_id)
 stu.delete()
 return redirect(student_list)

def student_list(request):
  all = Student.objects.all()
  return render(request,'day5/student_list.html',{'all':all})

def add_course(request, std_id):
    if request.method == 'POST':
        try:
            student = get_object_or_404(Student, std_id=std_id)
            course_id = request.POST.get('course_id')
            course = get_object_or_404(Course, id=course_id)
            student.std_enrolled_courses.add(course)
            return render(request, 'day5/student_info.html', {'student': student})  # Redirect to student detail page
        except:
            return render(request, 'day5/add_course.html',{'info':"No Course left"})       
    else:
         return render(request, 'add_course.html')
    
def add_available_course(request, std_id):
    student = Student.objects.get(std_id=std_id)
    available_courses = Course.objects.exclude(student__std_id=std_id)
    return render (request,'day5/add_course.html',{'student': student,'available_courses':available_courses})


def search_stu(request):
   return render(request, 'day5/student_search.html')

def view_front_page(request):
    return render(request,'day5/front.html')

def search_student(request):
    if request.method == 'GET' and 'std_id' in request.GET:
      try:
        std_id = request.GET.get('std_id')
        student = get_object_or_404(Student, std_id=std_id)
        return render(request, 'day5/student_info.html', {'student': student})
      except :
         return render(request, 'day5/student_search.html',{'info':"Student id is not registered yet"})
        
    else:
        return render(request, 'student_search.html')
    

