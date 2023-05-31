from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic

from main.models import Course
from .forms import SingUpForm
from .models import User


class UserRegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request, *args, **kwargs):
        form = SingUpForm(request.POST)
        if form.is_valid() and form.data['password']==form.data.get('show_password'):
            data=form.cleaned_data
            user = User.objects.create_user(
                phone_number=data['phone_number'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data['password'],
                show_password=data['show_password']
            )  # userni ro'yxatga olish
            login(request, user)  # login qilish
            messages.success(request, 'Your account has been created!')
            return redirect('home')
        else:
            messages.warning(request, form.errors)
            print(form.errors)
            return redirect('register')


def LogIn(request):
    if request.method == 'POST':

        # html formadan data larni olish
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        # authenticate orqali tekshiramiz
        user = authenticate(phone_number=phone_number, password=password)

        if user:
            # user mavjud bolsa login qilinadi
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Phone number or Password is incorrect")
            return redirect('login')
    else:
        return render( request, "login.html")


class UserCourseListView(LoginRequiredMixin, generic.ListView):
    model = Course
    template_name = 'user_courses.html'

    def get_queryset(self):
        user = self.request.user
        print(user)
        object_list = Course.objects.filter(students=user)
        print(object_list)
        return object_list
