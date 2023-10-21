from django.urls import path

from store import views

app_name = 'store'

urlpatterns = [
    path('', views.show_data, name='store_index'),
]
