from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    movie = forms.CharField(required=True, label= "The Movie")
    my_rating = forms.DecimalField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Out of 10'}))
    my_review = forms.CharField(required=True)
    

    class Meta:
        model = Review
        exclude = ("user", )