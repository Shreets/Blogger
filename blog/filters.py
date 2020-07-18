import django_filters
from django_filters import CharFilter
from .models import Blog

class BlogFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    # author = CharFilter(field_name='author', lookup_expr='icontains')
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['image', 'body', 'date_updated', 'date_created']
