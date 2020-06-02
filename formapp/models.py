'''from django.db import models

class Registrationfm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Img1 = models.ImageField(upload_to='images/')
    Img2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    '''

from mongoengine import Document,fields
from mongoengine import *

connect(
        db='django-form',
        host='m**********************************************',
        username='*************************',
        password='*************************'
)

class Registrationfm(Document):
    name = StringField(max_length=50 , required=True)
    email = EmailField(max_length=50 , required=True)
    Img1 = ImageField()
    Img2 = ImageField()

    def __str__(self):
        return self.name
