from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=20, 
    	widget=forms.TextInput(attrs={'class' : 'form-control'}))
    project_name = forms.CharField(max_length=40,
    	widget=forms.TextInput(attrs={'class' : 'form-control'}))
    min_gpa = forms.CharField(max_length=4,
    	widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '3.0'}))
    min_year = forms.CharField(max_length=12,
    	widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Sophomore'}))
    min_exp = forms.CharField(max_length=2, 
    	widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '2'}))
    kwords = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Machine Learning, Physics'}))
    req_classes = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Data Structures'}))
    