from django import forms
from .models import Product

class PostForm(forms.ModelForm):
  desc = forms.CharField(widget=forms.TextInput(attrs={'class':'materialize-textarea'}) )
  class Meta:
    model = Product
    fields = [
      "name",
      "desc",
      "category",
      "price",
      "image"
    ]