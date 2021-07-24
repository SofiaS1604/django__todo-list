from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:pk>', views.AuthorDeleteView.as_view(), name='del')
]
