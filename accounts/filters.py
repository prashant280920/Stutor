import django_filters
from .models import Profile
from django.contrib.auth.models import User, Group


class TutorFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = {
            'homeaddress': ['icontains'],
            'specialization': ['icontains']
        }
