from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class user(models.Model):
	userid= models.CharField(max_length=55)
	password= models.CharField(max_length=30)
 


class contactdetails(models.Model):
	full_name= models.CharField(max_length=55)
	position= models.CharField(max_length=30)
	city= models.CharField(max_length=30)
	state= models.CharField(max_length=30)
	zipcode= models.CharField(max_length=10)
	phone= models.CharField(max_length=12)
	email= models.EmailField(max_length=40)
	personal_profile = models.CharField(max_length=1000)

class educ(models.Model):
	school_name = models.CharField(max_length=55)
	school_location = models.CharField(max_length=55)
	Degree = models.CharField(max_length=55)
	CGPA=models.CharField(max_length=55)
	Field_of_Study = models.CharField(max_length=55)
	Expected_year_of_grad = models.CharField(max_length=55)
	

class workexp(models.Model):
	job_title = models.CharField(max_length=55)
	employer = models.CharField(max_length=55)
	city = models.CharField(max_length=55)
	state=models.CharField(max_length=55)
	startdate = models.DateField(max_length=55)
	enddate = models.DateField(max_length=55)
	jobdesc = models.CharField(max_length=2000)

class skills(models.Model):
	skill= models.CharField(max_length=55)
		

class extrafield(models.Model):
	field_name = models.CharField(max_length=100)
	explanation = RichTextField(blank=True ,null= True)

		