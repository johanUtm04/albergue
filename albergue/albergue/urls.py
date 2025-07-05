from django.contrib import admin
from django.urls import path
from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="Principal"),
    path('login/', views.login, name="Login"), # Nueva URL para el login
    path('register/', views.register_user, name = "register"),
    path('pacientes/', views.pacientes, name='pacientes'),

]
