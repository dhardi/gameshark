from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a catchy title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your detailed review here', 'rows': 5}),
        }
    
    # Sobrescrevendo o campo rating para personalizar o widget de estrelas
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect(attrs={'class': 'rating'}),
    )
