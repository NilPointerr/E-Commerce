from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from home.views import login_detail

urlpatterns = [
    path("",views.homepage,name='home'),
    path('contact',views.contact,name = 'contact'),
    path('about',views.about,name = 'about'),
    path('service',views.service,name = 'service'),
    path('register',views.register_1,name ='register'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logout,name='logout'),
    path('mobiles',views.mobiles,name='mobiles'),
    path('laptop',views.laptop,name='laptop'),
    # path('login_detail',views.viewdata,name='login_detail'),
    path('login_detail',login_detail.as_view(),name = 'login_detail'),
    path('product_desc/<int:myid>',views.product_desc,name='product_desc'),
    path('cart',views.cart,name='cart'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



