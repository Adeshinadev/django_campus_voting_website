from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    users=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    organization_name=models.CharField(max_length=100)
    type_of_organization=models.CharField(max_length=30)
    phone_no=models.CharField(max_length=15)

    def __str__(self):
        return '{} {} {}'.format(self.first_name,self.last_name,self.organization_name)

