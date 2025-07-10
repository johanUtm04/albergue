from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url='Login')  # si no es staff, manda al login
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

@staff_member_required(login_url='Login')
@permission_required('auth.add_user', raise_exception=True)
def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/user_form.html', {'form': form})

@staff_member_required(login_url='Login')
@permission_required('auth.change_user', raise_exception=True)
def user_edit(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

@staff_member_required(login_url='Login')
@permission_required('auth.delete_user', raise_exception=True)
def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
