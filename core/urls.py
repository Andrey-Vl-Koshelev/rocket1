from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='index'),
    path('addpage/', AddPage.as_view(), name='add_page'),

]
