from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('register/', views.register, name='register'),
	# login routes
	#path('login/', views.user_login, name='login'),
	path('login/', auth_views.LoginView.as_view(template_name='app_one/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='app_one/logout.html'), name='logout'),
	# edit
	path('student-id/', views.student_id, name='idcard'),
	path('profile/', views.edit, name='edit'),
	# dashboard
	path('', views.dashboard, name='dashboard'),

]