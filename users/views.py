from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import UserRegisterForm,UserUpdate,ProfileUpdate
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!You are now logged In!')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


@login_required
def Profile(request):
    if request.method=='POST':
        u_form=UserUpdate(request.POST,instance=request.user)  ## instace is used to populate the fields by the current values and then user can update it
        p_form=ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)  # request.Files for any image coming when user updates
        
        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
            
    else:
        u_form=UserUpdate(instance=request.user)  ## instace is used to populate the fields by the current values and then user can update it
        p_form=ProfileUpdate(instance=request.user.profile)


    context={
            'u_form':u_form,
            'p_form':p_form
    }
    return render(request,'users/profile.html',context)