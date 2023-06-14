from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    #main page
    path('', views.index, name='index')
]