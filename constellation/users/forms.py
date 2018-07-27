from django import forms


class ExpForm(forms.Form):
    title = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    company = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    desc = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class' : 'form-control'}))