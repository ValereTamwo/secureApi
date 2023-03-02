from django.urls import path,include
from .views import getAllTask,newTask,update,deleteTask,createUser,getUserdata,Deconnect,MeviewSet
from django.contrib.auth import views as auth


urlpatterns = [
     path("all/<int:id>/",getAllTask),
     path("addtask/",newTask),
     path("update/<int:u_id>/<int:t_id>/",update),
     path("delete/<int:u_id>/<int:t_id>",deleteTask),
     path("adduser",createUser), 
     path("me",MeviewSet.as_view({'get': 'list'})),
     path("logout",Deconnect),
        
] 
  