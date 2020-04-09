from django.db import models
from django.conf import settings

# Create your models here.


class job_place(models.Model):
	name = models.CharField(verbose_name = 'place',max_length = 50,unique=True)
	job = models.CharField(verbose_name='job description',max_length=100)
	comment = models.TextField(verbose_name='comments',blank=True,null=True)


	def __str__(self):
		return self.name + " | " + self.job


class job_user_allotment(models.Model):
	job = models.ForeignKey(job_place,on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	date = models.DateField(verbose_name='Date')


	def __str__(self):
		return self.user.email + "  |  " + self.job.name




