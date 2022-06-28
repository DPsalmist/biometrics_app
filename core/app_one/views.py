from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from .models import Profile


# Create your views here.
def register (request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			# Set the chosen password:using the set_password() allows encryption
			new_user.set_password(user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			# Create the user profile
			Profile.objects.create(user=new_user)
			return render (request,
							'app_one/register_done.html', {'new_user':new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'app_one/register.html', {'user_form':user_form})
 

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user =  authenticate(request,
								username = cd['username'],
								password = cd['password'])

			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse ('Authenticated ' \
					 'successfully !')
				else:
					return HttpResponse ('Disabled Account !')
			else:
				return HttpResponse ('invalid login!')
	else:
		form = LoginForm()
	return render(request, 'app_one/login.html', {'form':form})

def logout_user(request):
	logout(request)
	return render(request, 'app_one/logout.html')


@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,
										data = request.POST,
										files = request.FILES)
		if user_form.is_valid():
			user_form.save()
			messages.success(request, f'User Profile updated successfully!')
		else: 
			messages.warning(request, f'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	return render(request, 'app_one/edit.html',
							{'user_form':user_form,
							'profile_form':profile_form})


@login_required
def student_id(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,
										data = request.POST,
										files = request.FILES)
		if profile_form.is_valid():
			profile_form.save()
			messages.success(request, f'Student detail updated successfully!')
		else: 
			messages.warning(request, f'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	return render(request, 'app_one/student_id.html',
							{'user_form':user_form,
							'profile_form':profile_form})


@login_required
def dashboard(request):
	user = request.user
	#user_exam = Exam.objects.filter(poster=user).order_by('-exam_date')
	#pending_exams = Exam.objects.filter(completed=False)
	#pending_exams = pending_exams.count()
	#user_exam = user_exam
	#print('these are it:', user_exam)
	context = {
		'section':'dashboard',
		'user':user, 
		#'user_exam':user_exam,
		#'pending_exams': pending_exams
		}
	return render(request, 'app_one/dashboard.html', context)
