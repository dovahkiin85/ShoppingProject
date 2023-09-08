from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('members.urls')),
    path('', include('products.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login.html'),
    path('login/',include('home.urls')),
    path('admin/', admin.site.urls),
]
