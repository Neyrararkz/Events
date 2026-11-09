from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('<int:pk>/<slug:slug>', views.detail, name="event_detail"),
    path('create/', views.create, name="event_create")
]
