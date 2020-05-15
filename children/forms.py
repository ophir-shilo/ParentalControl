from django import forms
from .models import BlockedUrl


class BlockedUrlForm(forms.ModelForm):
    class Meta:
        model = BlockedUrl
        fields = ['url']
        widgets = {
            'url': forms.TextInput(attrs={'placeholder': 'e.g., www.facebook.com'})
        }
