from django.urls import path
from . import views
urlpatterns=[
    path('',views.register,name='register'),
    path("signin",views.login,name='siginin'),
    path('signout',views.logout,name='signout')
]