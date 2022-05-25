from django.db import models
from jp_app.models import User

class CandidateProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='candidates')
    pro_pic=models.ImageField(upload_to='pro_p')
    qualification=models.CharField(max_length=100)
    age=models.PositiveIntegerField(default=18)
    skills=models.CharField(max_length=100,null=True)
    cv=models.FileField(upload_to='cvs',null=True)

