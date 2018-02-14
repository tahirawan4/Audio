"""Audio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from age_estimation.forms import UserLoginForm
from age_estimation.views import index, submit_time, login, signup
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('submit_time/', submit_time, name='submit_time'),
                  # path('login/', login, name='login'),
                  path(r'login/', auth_views.login,
                       {'template_name': 'login.html', 'authentication_form': UserLoginForm},
                       name='login'),
                  path(r'logout/', auth_views.logout, name='logout'),
                  path('signup/', signup, name='signup'),
                  path('', index, name='index'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
