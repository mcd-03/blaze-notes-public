from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.index, name='index'),
	path('review/', views.review, name='review'),
	path('login/', auth_views.LoginView.as_view(template_name='review/login.html'), name='login'),
	path('profile/', views.profile, name='profile'),
    path('class-stats/', views.class_stats, name='class_stats'),
]
