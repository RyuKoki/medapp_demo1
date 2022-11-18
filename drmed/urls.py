"""drmed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from medapp import views
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.home, name="home"),
    # sign in
    path('login_form/', views.login_form), 
    path('login_form/login/', views.login), 
    # sign out
    path('logout/', views.logout), 
    # sign up
    path('signup/', views.signup), 
    # read / show elder's info
    path('elderinfo/', views.view_elder_info), 
    path('signup/signup_form/', views.signup_form), 
    path('elderly/register/', views.add_new, name="add_new"),
    # step 1
    path('elderly/register/1/', views.elder_register, name="elder_register"),
    path('elderly/register/2/', views.elder_register2, name="elder_register2"),
    # step 2
    path('elderly/register/3/', views.elder_register3, name="elder_register3"),
    path('elderly/register/4/', views.elder_register4, name="elder_register4"),
    # step 3
    path('elderly/register/5/', views.elder_register5, name="elder_register5"), 
    path('elderly/register/summary/', views.save_elder_info, name="save_elder_info"), 
    # forget password
    path('reset_password/', views.forget_password, name="forget_password"), 
    path('login/reset/', views.send_reset_pwd, name="send_reset_pwd"), 
    path('setting_password/', views.new_password, name="new_password"), 
    path('setting_password/success/', views.repassword_success, name="repassword_success"), 
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
