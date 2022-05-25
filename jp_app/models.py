from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone=models.CharField(max_length=14,default='+91-')

    options=(
        ('Employer','Employer'),
        ('Candidate','Candidate')
    )
    role=models.CharField(max_length=15,choices=options,default='Candidate')

    @property
    def is_candidate(self):
        return self.role=='Candidate'
    def is_employer(self):
        return self.role=='Employer'


