from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.views import View
from .models import *

class TodoView(View):
    def get(self, request):
        if request.user.is_authenticated:
            plans = Plan.objects.filter(user = request.user)
            return render(request, 'todo.html', {'plans' : plans})
        else:
            return redirect('/')
    def post(self, request):
        Plan.objects.create(
            title = request.POST['title'],
            description = request.POST['desc'],
            time = request.POST['time'],
            status = request.POST['status'],
            user = request.user
        )
        return redirect('todos')

class PlanView(View):
    def get(self, request):
        return render(request, 'auth.html')
    def post(self, request):
        loginn = request.POST['login']
        parol = request.POST['parol']
        user = authenticate(username = loginn, password = parol)
        if user is None:
            return redirect('/')
        else:
            login(request, user)
            return redirect('todos')

class DeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            Plan.objects.get(id = pk).delete()
            return redirect('todos')
        else:
            return redirect('/')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        login = request.POST['login']
        parol1 = request.POST['parol1']
        parol2 = request.POST['parol2']
        if parol1 == parol2:
            User.objects.create(
                username = login,
                password = parol1
            )
            return redirect('kirish')
        return redirect("register")

def Logout(request):
    logout(request)
    return redirect('/')