from django.urls import path
from . import  views

app_name="test_share"
urlpatterns = [
    path('', views.index, name="index"),
    path('subject_detail/<int:subject_pk>/', views.subject_detail, name="subject_detail"),
    path('test_add/<int:subject_pk>/', views.test_add, name="test_add"),
    path('like/<int:subject_pk>/<int:like_pk>/<str:do>/', views.push_like, name="push_like"),
]