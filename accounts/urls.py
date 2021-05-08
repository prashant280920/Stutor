from django.urls import path, include
from . import views
from .views import login_view,register_view,ProfileView, ProfileUpdateView

urlpatterns = [
    path("", views.index, name = 'index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('update_profile/', ProfileUpdateView, name='update_profile'),
    path('profile/', ProfileView, name='profile')
]