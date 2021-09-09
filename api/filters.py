import django_filters as filters

from .models import Category, Genre, Title


class TitleFilter(filters.FilterSet):
    genre = filters.ModelChoiceFilter(
        field_name='genre__slug',
        to_field_name='slug',
        queryset=Genre.objects.all()
    )

    category = filters.ModelChoiceFilter(
        field_name='category__slug',
        to_field_name='slug',
        queryset=Category.objects.all()
    )

    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ('genre', 'category', 'year', 'name')
