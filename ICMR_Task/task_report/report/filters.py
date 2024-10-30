import django_filters 
from .models import *

class searchFilter(django_filters.FilterSet):
    class Meta:
        model = Report
        fields = '__all__'
        