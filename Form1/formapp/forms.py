from django import forms
from .models import Registrationfm

class RegistrationModal(forms.ModelForm):
    class Meta:
        model = Registrationfm

        fields =(
            'name',
            'email',
            'Img1',
            'Img2',
        )

        widgets={
            'name':forms.TextInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'enter clinic name / hospital'
                               }),
            'email':forms.EmailInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'email'
                               }),
        }
        '''
            'Img1': forms.ImageField(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'FRONT/INSIDE PICTURE'
            }),
            'Img2': forms.ImageField(attrs={
                                   'class': 'form-control',
                                    'placeholder': 'BUSINESS CARD IMAGE'
            }),'''

