from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

# class User(AbstractUser):
# 	email = models.CharField(max_length = 200, blank=True, unique=True)
# 	first_name = models.CharField(max_length=200, blank=True)
# 	last_name = models.CharField(max_length=200, blank=True)
# 	username = models.CharField(max_length = 200, blank=True, unique=True)
# 	date_created = models.DateTimeField(auto_now_add=True)
# 	typing_id = models.CharField(max_length=200, blank=True, default=uuid.uuid4())

# 	USERNAME_FIELD = 'username'
# 	REQUIRED_FIELDS = []

# 	def __str__(self):
# 		return self.username
	
class Profile(models.Model):
	gender = (
			('select', 'select'),
			('male', 'male'),
			('female', 'female')
		)
	colleges = (
			('select', 'select'),
			('CONAS','CONAS'),
			('CBSS','CBSS'),
		)
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	bio = models.CharField(max_length=200, blank=True)
	photo = models.ImageField(upload_to='profiles/', default='media/default.jpeg', blank=True)
	level = models.CharField(max_length=200, blank=True, default=100)
	gender = models.CharField(max_length=100, choices=gender, default='select')
	college = models.CharField(max_length=100, choices=colleges, default='select')
	department = models.CharField(max_length=200, blank=True)
	nationality = models.CharField(max_length=100, blank=True, default='Nigeria')
	phone_no = models.CharField(max_length=100, blank=True)
	matric_no = models.CharField(max_length=100, blank=True, null=True)
	staff_id = models.CharField(max_length=100, blank=True, null=True)
	verified_student = models.BooleanField(default=False)
	verified_staff = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)
