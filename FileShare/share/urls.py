from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('send/', views.create_session, name='create_session'),
   path('receive/<str:key>/', views.join_session, name='join_session'),
   path('upload/<str:key>/', views.upload_file, name='upload_file'),
   path('get_files/<str:key>/', views.get_files, name='get_files'),
]
