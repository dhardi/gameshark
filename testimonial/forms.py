from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['text', 'rating']

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Write your testimonial here...'})
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})
