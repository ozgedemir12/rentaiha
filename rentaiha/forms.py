from django import forms

from rentaiha.models import Iha




class IhaForm(forms.ModelForm):  
    class Meta:  
        model = Iha
        fields = ['brand','model', 'weight', 'category']