from django import forms
from .models import Buy
class ChouseForm(forms.ModelForm):
    class Meta:
        model = Buy
        exclude = ['produck']
        fields = '__all__'
