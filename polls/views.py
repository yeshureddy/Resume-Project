from django.shortcuts import render
from .models import user,contactdetails,educ, workexp,skills,extrafield
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .forms import Extrafielfform
# Create your views here.
#this is for page opening
@csrf_exempt
def userlogin(request):
	
	userid = request.POST.get('uid')
	password= request.POST.get('password')
	loginx=user(userid=userid,password=password)
	return render(request,'login.html')

@csrf_exempt
def firstpage (request):
	contactdetails.objects.all().delete()
	educ.objects.all().delete()
	workexp.objects.all().delete()
	skills.objects.all().delete()
	extrafield.objects.all().delete()
	return render(request,'template.html')


@csrf_exempt
def edu(request):
	if not request.POST.get('full'):
		return render(request,'Tell us about your education.html')
	else:
		full_name = request.POST.get('full')
		position = request.POST.get('position')
		city = request.POST.get('city')
		state = request.POST.get('state')
		zipcode = request.POST.get('zipcode')
		#email = request.POST.get('email')
		phone = request.POST.get('phone')
		personal_profile = request.POST.get('person')
		#email=email,contactx tesesanu,userid mail vadi chuddam
		contactx=contactdetails.objects.create(full_name=full_name, position=position, city=city,state=state,zipcode=zipcode ,personal_profile=personal_profile,phone=phone)
		return render(request,'Tell us about your education.html')
	


@csrf_exempt
def job345(request):
	if not request.POST.get('school_name',False):
		return render(request,'about job.html')
	else:
		school_name = request.POST.get('school_name',False)
		school_location = request.POST.get('school_location',False)
		Degree = request.POST.get('Degree',False)
		CGPA = request.POST.get('CGPA',False)
		Field_of_Study = request.POST.get('Field_of_Study',False)
		Expected_year_of_grad = request.POST.get('Expected_year_of_grad',False)
		contactx = educ.objects.create(school_name=school_name,school_location=school_location,Degree=Degree,CGPA=CGPA,
			Field_of_Study=Field_of_Study,Expected_year_of_grad=Expected_year_of_grad)
		return render(request,'about job.html')
	#return HttpResponseRedirect('/login/')

@csrf_exempt
def skillsfun(request):
	if not request.POST.get ('job_title'):
		return render(request,'skills.html')
	else:
		job_title = request.POST.get('job_title',False)
		employer = request.POST.get('employer',False)
		city = request.POST.get('city',False)
		state = request.POST.get('state',False)
		enddate = request.POST.get('enddate',False)
		startdate = request.POST.get('startdate',False)
		jobdesc = request.POST.get('jobdesc',False)
		something=workexp.objects.create(job_title=job_title ,employer=employer ,city=city, state=state ,enddate=enddate ,startdate=startdate ,jobdesc=jobdesc)
		return render(request,'skills.html')


@csrf_exempt
def home(request):
	
	#c_items = contactdetails.objects.all()
	#length = contactdetails.objects.all().count()
	#print(length)
	userr=user.objects.all()
	contact1 = contactdetails.objects.all()
	contacte1 = educ.objects.all()
	job1 = workexp.objects.all()
	skill1=skills.objects.all()
	adds = extrafield.objects.all()
	#return render(request,'home.html',{'c_items':c_items,'contacte1':contacte1,'job1':job1,'skills':skill1})
	#if not request.POST.get('field_name'):
	#	return render(request,'home.html',{'i':contact1,'contacte1':contacte1,'job1':job1,'skills':skill1,'adds':adds})

	#else:
	if not request.POST.get('field_name'):
		pass
	else:
		field_name= request.POST.get('field_name',False)
		explanation= request.POST.get('explanation',False)
		xyz = extrafield.objects.create(field_name=field_name,explanation=explanation)
	adds1 = extrafield.objects.all()
	return render(request,'home.html',{'gmail':userr,'i':contact1,'contacte1':contacte1,'job1':job1,'skills':skill1,'adds':adds1})
	#return render (request,'Extra_field')

@csrf_exempt
def educrev (request):
	school_name = request.POST.get('school_name',True)
	school_location = request.POST.get('school_location',True)
	Degree = request.POST.get('Degree',True)
	CGPA = request.POST.get('CGPA',True)
	Field_of_Study = request.POST.get('Field_of_Study',True)
	Expected_year_of_grad = request.POST.get('Expected_year_of_grad',True)
	contactx = educ.objects.create(school_name=school_name,school_location=school_location,Degree=Degree,CGPA=CGPA,
		Field_of_Study=Field_of_Study,Expected_year_of_grad=Expected_year_of_grad)
	return HttpResponseRedirect('/user/login/')


@csrf_exempt
def jobadd (request):
	job_title = request.POST.get('job_title',False)
	employer = request.POST.get('employer',False)
	city = request.POST.get('city',False)
	state = request.POST.get('state',False)
	enddate = request.POST.get('enddate',False)
	startdate = request.POST.get('startdate',False)
	jobdesc = request.POST.get('jobdesc',False)
	something=workexp.objects.create(job_title=job_title ,employer=employer ,city=city, state=state ,enddate=enddate ,startdate=startdate ,jobdesc=jobdesc)
	return HttpResponseRedirect('/user/login/next/')


@csrf_exempt
def skillsadd(request):
	skill = request.POST.get('skill',False)
	something2= skills.objects.create(skill=skill)
	return HttpResponseRedirect('/user/login/next/job')

@csrf_exempt
def addons(request):
	if not request.POST.get('skill'):
		return render(request,'Extra_field.html')
	else:
		skill= request.POST.get('skill',False)
		xyz = skills.objects.create(skill=skill)
		return render (request,'Extra_field.html')


@csrf_exempt
def addonemoreaddon(request):

	field_name= request.POST.get('field_name',False)
	explanation= request.POST.get('explanation',False)
	xyz = extrafield.objects.create(field_name=field_name,explanation=explanation)
	return HttpResponseRedirect('/user/login/next/job/skill')

@csrf_exempt
def addonstest(request):
	form = Extrafielfform(request.POST or None)
	if form.is_valid():
		form.save()
		form = Extrafielfform()
	if not request.POST.get('skill'):
		return render(request,'Extra_field.html',{'form':form})
	else:
		skill= request.POST.get('skill',False)
		xyz = skills.objects.create(skill=skill)
		return render (request,'Extra_field.html',{'form':form})










from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

userr=user.objects.all()
contact1 = contactdetails.objects.all()
contacte1 = educ.objects.all()
job1 = workexp.objects.all()
skill1=skills.objects.all()
adds = extrafield.objects.all()

data={'gmail':userr,'i':contact1,'contacte1':contacte1,'job1':job1,'skills':skill1,'adds':adds}

class viewPDF(View):
	def get(self , request ,*args , ** kwargs):
		pdf = render_to_pdf('home.html',data)
		return HttpResponse(pdf,content_type='application/pdf')



class DownloadPDF(View):
	def get(self,request, *args , **kwargs):
		pdf = render_to_pdf('home.html',data)
		return HttpResponse(pdf,content_type='application/pdf')
		filename = "Invoice_%s.pdf"%("1234512321")
		response['Content-Disposition'] = content
		return response

def index(request):
	context = {}
	return render (request,'home.html',context)



