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
    path('login',views.login,name='login')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# /home/dev28/Documents/Django_projects/firstwebsite/static/earbuds.jpeg