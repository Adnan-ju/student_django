from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/',views.index),
    path('index2/',views.index2),
]
