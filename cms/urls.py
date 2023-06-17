from django.urls import path, include
from . import views

app_name = 'cms'
urlpatterns = [
    path('events/', views.user_events, name='user_events'),
    path('event/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('add_event/', views.add_event, name='add_event'),
    path('event/<int:event_id>/', views.event_details, name='event_details'),
    path('user_tickets/', views.user_tickets, name='user_tickets'),
    path('buy_tickets/<int:event_id>/', views.buy_tickets, name='buy_tickets'),
    path('', views.index, name='index'),

]