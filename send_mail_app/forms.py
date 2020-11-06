from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    message = forms.CharField(label="", widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Qu'attendez vous de nous?" , "rows":4}))
    class Meta:
        model = Contact
        fields = ['nom', 'email', 'message']
    