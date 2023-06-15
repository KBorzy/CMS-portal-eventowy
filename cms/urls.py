from django.urls import path, include
from . import views

app_name = 'cms'
urlpatterns = [
    path('events/', views.user_events, name='user_events'),
    path('event/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('add_event/', views.add_event, name='add_event'),
    path('event/<int:event_id>/', views.event_details, name='event_details'),
    path('', views.index, name='index'),
]