from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.homepage,name='home'),
    path('contact',views.contact,name = 'contact'),
    path('about',views.about,name = 'about'),
    path('service',views.service,name = 'service'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logout,name='logout'),
    path('mobiles',views.mobiles,name='mobiles'),
    path('laptop',views.laptop,name='laptop'),
    path('login_detail',views.viewdata,name='login_detail')
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

