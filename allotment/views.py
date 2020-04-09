from django.shortcuts import render,redirect
from .models import job_place,job_user_allotment
from security.models import User,Profile,UserManager
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

def set_up(request):
	if request.user.is_admin:
		usrf = 'r'
		usrl = '@gmail.com'

		for i in range(1,8):
			usr = usrf + str(i) + usrl
			fullname = usrf + str(i)
			password = usrf + str(i)
			q = User.objects.filter(email=usr)
			if q.__len__()==0 :
				user = User(email = usr,fullname=fullname)
				user.set_password(password)
				user.save()
				pf = Profile(user = user)
				pf.save()

		plc = 'A'
		jb = 'gauriding'
		for i in range(1,8):
			place = plc + str(i)
			job = jb + str(i)
			q = job_place.objects.filter(name=place,job=job)
			if q.__len__()==0 :
				jp = job_place(name=place,job=job)
				jp.save()

	return redirect('home')

@login_required
def schedule_duties(request):
	if not request.user.is_admin:
		return redirect('home')

	current_date = datetime.date.today()
	delta = datetime.timedelta(days=1)
	
	# scheduling duties for next 7 seven days.
	for i in range(0,7):
		date = current_date + i*delta
		q = job_user_allotment.objects.filter(date=date)
		if q.__len__() !=0 :
			continue
		#job_user_allotment.objects.filter(date=date).delete()

		available_users = list(User.objects.filter(is_admin=False))
		available_jobs = list(job_place.objects.all())
		x = min(len(available_jobs),len(available_users))
		for i in range(0,x):
			ele = job_user_allotment(user=available_users[i],job=available_jobs[i],date=date)
			ele.save()

	data = job_user_allotment.objects.filter(date__gte = current_date , date__lt = current_date+7*delta)

	return render(request,'allotment/schedule_duties.html',{'data':data})
