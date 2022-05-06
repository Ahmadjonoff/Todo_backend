from django.contrib import admin
from django.urls import path
from app.views import PlanView, RegisterView, TodoView, DeleteView, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PlanView.as_view(), name = 'kirish'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('todos/', TodoView.as_view(), name = 'todos'),
    path('logout/', Logout, name = 'logout'),
    path('delete/<int:pk>/', DeleteView.as_view(), name = 'delete'),
]
