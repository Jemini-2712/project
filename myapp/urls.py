from . import views
from django.urls import path

urlpatterns = [

    path('', views.sign_in, name='sign-in'),
    path('index/',views.index,name='index'),
    path('sign-up/',views.sign_up,name='sign-up'),
    path('otp/',views.otp,name='otp'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('forgot-psw/',views.forgot_psw,name='forgot-psw'),
    path('virtual-reality/',views.virtual_reality,name='virtual-reality'),
    path('rtl/',views.rtl,name='rtl'),
    #path('change-password/',views.change_password,name='change-password'),
    path('service/',views.service,name='service'),
]
