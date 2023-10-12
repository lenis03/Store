from django.urls import path

from store import views

app_name = 'store'

urlpatterns = [
    path('', views.store, name='store'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('get_num/<int:num>/', views.get_num, name='get_num'),
    path('hello_to_user/<str:name>/', views.say_hello_to_user, name='hello_to_user'),
  
]
