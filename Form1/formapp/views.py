from django.contrib import messages
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
