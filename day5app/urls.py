from django.urls import path
from . import views
urlpatterns = [
   
    path('', views.view_front_page, name='view_front_page'),
    path('search_student/',views.search_stu,name="search_stu"),
    path('student/<int:std_id>/add_course/', views.add_course, name='add_course'),
    path('add_available_course/<int:std_id>/',views.add_available_course,name='add_available_course'),
    path('student_registration/', views.student_register,name='student_register'),
    path('remove/<int:std_id>/remove_course/<int:course_id>/', views.remove_course, name='remove_course'),
    path('search_result/', views.search_student, name='search_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('remove_students/<int:std_id>',views.remove_student,name='remove_student'),
    path('add_student/',views.add_student,name='add_student'),
    path('save_student/',views.save_student,name='save_student'),


]
