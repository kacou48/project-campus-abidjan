from django import forms
from . models import Comment




class CommentForm(forms.ModelForm):
    contenu = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control border border-primary text-dark flex-column flex-md-row', 'placeholder': 'entrez votre commentaire', 'rows':1, 'cols': 50}))
    class Meta:
        model = Comment
        fields = ('contenu',)