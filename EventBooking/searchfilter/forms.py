from django import forms
from searchfilter .models import Book

class BookSearchForm(forms.Form):
    title = forms.CharField(required=False, label='Title')
    author = forms.CharField(required=False, label='Author')