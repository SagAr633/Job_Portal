from django import forms
from employer.models import EmployerProfile,Jobs

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model= EmployerProfile
        exclude=('user',)

class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        exclude=('posted_by','created_date')
        widgets={
            'last_date':forms.DateInput(attrs={'class':'form-control','type':'date'})
        }