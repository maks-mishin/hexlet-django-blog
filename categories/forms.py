from django import forms
from categories.models import Category


CATEGORY_CHOICES = [
    ('draft', 'draft'),
    ('published', 'published')
]


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=200, required=True)
    state = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES))

    class Meta:
        model = Category
        fields = ['name', 'description', 'state']
