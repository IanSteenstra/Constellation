from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')

class ProfileForm(forms.Form):
	STUDENT = 1
	TEACHER = 2
	ROLE_CHOICES = (
		(STUDENT, 'Student'),
		(TEACHER, 'Teacher'),
	)
	FRESHMAN = 1
	SOPHOMORE = 2
	JUNIOR = 3
	SENIOR = 4
	YEAR_CHOICES = (
		(FRESHMAN, 'Freshman'),
		(SOPHOMORE, 'Sophomore'),
		(JUNIOR, 'Junior'),
		(SENIOR, 'Senior'),
	)
	username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)
	first_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)
	last_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)
	email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)
	# password = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	gpa = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)
	year = forms.ChoiceField(widget=forms.Select, choices=YEAR_CHOICES, required=False)
	role = forms.ChoiceField(widget=forms.Select, choices=ROLE_CHOICES, required=False)
	desc = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class' : 'form-control'}), required=False)

class ExpForm(forms.Form):
    title = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    company = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    start_date = forms.DateField()
    end_date = forms.DateField()
    desc = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class' : 'form-control'}))
