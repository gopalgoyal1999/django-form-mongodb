from django.db import models

class Registrationfm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Img1 = models.ImageField(upload_to='images/')
    Img2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name