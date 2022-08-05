from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="project.index"),
    path('store/', views.store, name="project.store"),
    path('create/', views.create, name="project.create"),
    path('<str:uuid>/', views.show, name="project.show"),
    path('<str:uuid>/edit', views.edit, name="project.edit"),
    path('<str:uuid>/update', views.update, name="project.update"),
    path('<str:uuid>/delete', views.delete, name="project.delete"),
]
