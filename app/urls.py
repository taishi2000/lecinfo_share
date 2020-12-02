from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='app'
urlpatterns = [
    path('', views.index, name='index'),
    path('subject_detail/<int:subject_pk>/', views.subject_detail, name="subject_detail"),
    path('comment_add/<int:subject_pk>/', views.comment_add, name="comment_add"),
    path('edit/<int:comment_pk>/', views.edit, name="edit"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name="app/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('like/<int:subject_pk>/<int:like_pk>/<str:do>/', views.push_like, name="push_like"),
]