'''from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Registrationfm
from .forms import RegistrationModal
# Create your views here.
def home(request):
    reg = Registrationfm.objects.all()
    return render(request, '../template/home.html',{'reg':reg})


def addmodalform(request):
    if request.method == 'POST':
        mymodalform = RegistrationModal(request.POST,request.FILES)

        if mymodalform.is_valid():
            mymodalform.save()
            messages.add_message(request, messages.SUCCESS, "you have signup successfully")
            return redirect('modalform')

    else:
        mymodalform = RegistrationModal()
    return render(request,'../template/modalform.html',{'mymodalform':mymodalform})
'''
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from .models import Registrationfm
from .serializers import dataserializer

class DataView(viewsets.ModelViewSet):

    lookup_field = 'id'
    serializer_class = dataserializer

    def get_queryset(self):
        return Registrationfm.objects.all()

    def post(self, request):
        serializer = dataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
