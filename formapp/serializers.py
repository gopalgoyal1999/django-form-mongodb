from rest_framework_mongoengine import serializers
from .models import Registrationfm

class dataserializer(serializers.DocumentSerializer):
    class Meta:
        model = Registrationfm
        fields = ('name','email','Img1','Img2')
