from django.urls import path, include
from . import views

app_name = 'cms'
urlpatterns = [
    #main page
    path('', views.index, name='index'),
    path('add_event/', views.add_event, name='add_event'),
    path('event/<int:event_id>/', views.event_details, name='event_details'),
]