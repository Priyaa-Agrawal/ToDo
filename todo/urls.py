
from django.urls import path
from . import views

urlpatterns = [
    path('index/<username>',views.index,name='index'),
    path('task/<username>',views.task,name='task'),
    path('complete/<todo_id>/<todo_username>',views.complete,name='complete'),
    path('deletecomplete/<username>',views.deletecomplete,name='deletecomplete'),
    path('deleteall/<username>',views.deleteall,name='deleteall'),
    
]
