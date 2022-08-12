from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profile.index"),
    path('<str:uuid>/edit', views.edit, name="profile.edit"),
    path('<str:uuid>/update', views.update, name="profile.update"),
]