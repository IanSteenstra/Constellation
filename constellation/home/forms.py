from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=20)
    project_name = forms.CharField(max_length=40)
    min_gpa = forms.CharField(max_length=4)
    min_year = forms.CharField(max_length=4)
    min_exp = forms.CharField(max_length=4)
    kwords = forms.CharField(widget=forms.Textarea())
    req_classes = forms.CharField(widget=forms.Textarea())