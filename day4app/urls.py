from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='index'),
    path('del/<int:id>', views.remove,name='remove'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('addNew/',views.add,name='add'),
    path('save/',views.save,name='save'),
    
    # path('day4app/', include('day4app.urls')),

]
