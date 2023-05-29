import django_filters
from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .serializers import UserSerializer
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'core/addpage.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление заказа'
        context['menu'] = menu
        return context


menu = [
    {'title': 'Купить сейчас', 'url_name': 'index'},
    {'title': 'Выбрать размер', 'url_name': 'index'},
    {'title': 'Заказать', 'url_name': 'index'},
]


class BlogHome(ListView):
    model = Blog
    template_name = 'core/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context


class UserFilter(filters.FilterSet):
    username = django_filters.CharFilter(field_name="username")

    class Meta:
        model = User
        fields = ['username']


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = UserFilter

    def get_queryset(self):
        return User.objects.all()
