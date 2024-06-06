from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistrationsView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect('homepage')
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, 'users/login.html', {'form': form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        # Optionally handle GET requests if you want to provide a logout link
        logout(request)
        return redirect('homepage')



class ProfileView(View):
    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        context = {
            'user': user
        }
        return render(request, 'users/profile.html', context=context)


# class RegistrationsView(View):
#     def get(self, request):
#         return render(request, 'users/register.html')
#
#     def post(self, request):
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = CustomUser.objects.create(
#             username=username,
#             email=email
#         )
#         user.set_password(password)
#         user.save()
#         return redirect('homepage')


