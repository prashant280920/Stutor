from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .forms import UserRegisterForm, UpdateProfileForm
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from .filters import TutorFilter
from .models import Profile
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    current_user = request.user
    tutors = Profile.objects.filter(user__groups__name='tutor')
    filtered_tutors = TutorFilter(request.GET, queryset=tutors)
    context = {
        'user': current_user,
        'queryset': tutors,
        'filter': filtered_tutors,
    }
    paginated_filtered_tutors = Paginator(filtered_tutors.qs, 2)
    page_number = request.GET.get('page')
    tutor_page_obj = paginated_filtered_tutors.get_page(page_number)
    context['tutor_page_obj'] = tutor_page_obj
    return render(request, 'index.html', context)


@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


@unauthenticated_user
def register_view(request):
    form = UserRegisterForm()
    # role_form = RoleRegister()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_save = form.save()
            if form.cleaned_data.get('is_tutor') == 'YES':
                set_group = Group.objects.get(name='tutor')
                user_save.groups.add(set_group)
            else:
                set_group = Group.objects.get(name='student')
                user_save.groups.add(set_group)

            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def ProfileView(request):
    profile = request.user.profile
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'profile/profile.html', context)


@login_required
def ProfileUpdateView(request):
    return render(request, 'profile/test.html', {})
