from django import forms


class ReviewForm(forms.Form):
    review = forms.CharField(label='Review', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))
    rating = forms.FloatField(label='Rating', min_value=1.0, max_value=5.0,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
