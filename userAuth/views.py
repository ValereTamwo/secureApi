from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializers,UserSerialzer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
     

# Create your views here.
# @permission_classes(IsAuthenticated)
@api_view(['GET'])
def getAllTask(request,id):    
    tasks = Task.objects.filter(user=id)
    serialTasks = TaskSerializers(tasks,many=True)
    return Response(serialTasks.data)

@api_view(["POST"])   
def newTask(request):
    seria = TaskSerializers(data=request.data)
    if(seria.is_valid()):
        seria.save()
    return Response(seria.data)


@api_view(["PUT"])
def update(request,u_id,t_id):
    task = Task.objects.filter(user=u_id, task_id=t_id).first()
    serial = TaskSerializers(instance=task,data=request.data ,many=False)
    if(serial.is_valid()):
        serial.save()
    return Response(serial.data)


@api_view(["DELETE"])
def deleteTask(request,u_id,t_id):
    task = Task.objects.filter(user=u_id,task_id=t_id)
    task.delete()
    
    return Response("Suppression Reussi ...")

@api_view(['POST'])
def createUser(request):
    user = User.objects.create_user(request.data['name'],request.data['email'],request.data['password']) 
    user.save()
    return Response(True)

@api_view(['POST'])
def getUserdata(request):
    user = authenticate(request,username=request.data['name'],password = request.data['password'])
    if user is not None:
        login(request,user)
        serial = UserSerialzer(user)
        return Response(serial.data)
    else:
        return Response('user not authenticated ...')
    
def Deconnect(request):
    logout(request) 
    
       
class MeviewSet(viewsets.ViewSet):   
    
    permission_classes =(IsAuthenticated,)
    
    def list(self,request):
        user = User.objects.get(username=request.user)
        serial = UserSerialzer(user).data
        return Response(serial)