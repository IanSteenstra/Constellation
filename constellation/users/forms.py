from django import forms


class ExpForm(forms.Form):
    title = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    company = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    time = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    desc = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class' : 'form-control'}))

class Profile(forms.Form):
	gpa = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	year = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	desc = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class' : 'form-control'}))
