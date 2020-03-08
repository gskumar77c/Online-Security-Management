from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserCreationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,User


@login_required
def home(request):
	if request.user.is_admin:
		return render(request,'security/adminhome.html')
	else:
		return render(request,'security/home.html')


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			usr = User.objects.get(email = form.cleaned_data.get('email'))
			pf = Profile(user = usr)
			pf.save()
			messages.success(request, 'Account Created Successfully!')
			return redirect('login')
		else:
			usr = form.cleaned_data.get('email')
			if usr==None:
				messages.warning(request, 'Invalid email address')
			else :
				pas1 = form.cleaned_data.get('password1')
				pas2 = form.cleaned_data.get('password2')
				if(pas1 != pas2) :
					messages.warning(request, 'confirm password must be same as password')

	form = UserCreationForm()
	return render(request,'security/register.html',{'form':form})



@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,
			instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, 
			instance = request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Account has been updated')
			return redirect('profile')

	else :
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)

	context = {'u_form' : u_form,
				'p_form' : p_form
				}
	return render(request,'security/profile.html',context)



@login_required
def schedule(request):
	if not request.user.is_admin:
		return redirect('home')

	users = User.objects.filter(is_admin=False,is_active=True)
	useravailability = {}
