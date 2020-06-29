from django.urls import path
from . import views

urlpatterns=[
	#path('',views.userlogin,name='userlogin'),
     path('',views.firstpage,name='firstpage'),
     path('login/',views.edu,name = 'edu'),
     path('login/add/',views.educrev,name='educrev'),
     path('login/next/',views.job345, name='job345'),
     path('login/next/job/',views.skillsfun,name='skillfun'),
     path('login/next/add/',views.jobadd,name='jobadd'),
     path('login/next/job/add/',views.skillsadd,name='skillfun'),
     #path('login/next/job/skill/',views.addons,name='home'),
     path('login/next/job/skill/',views.addonstest,name='home'),
     path('login/next/job/skill/addonemorefield/',views.addonemoreaddon,name='home'),
     path('login/next/job/skill/fieldadd/',views.home,name='home'),
     path('login/next/job/skill/fieldadd/pdf_view/',views.viewPDF.as_view(),name='pdf_view'),
]