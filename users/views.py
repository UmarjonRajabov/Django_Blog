from django.shortcuts import render,redirect

# Create your views here.
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    # form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'yangi akkount yaratildi. Siz login qila olasiz')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')