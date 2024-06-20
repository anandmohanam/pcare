"""pcare URL Configuration

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
from django.contrib import admin
from django.urls import path
from pcareapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('loginadmin/', views.loginadmin, name='loginadmin'),
    path('loginauthority/', views.loginauthority, name='loginauthority'),
    path('loginclerk/', views.loginclerk, name='loginclerk'),
    path('', views.mainhome, name='mainhome'),
    path('publicreg/', views.publicreg, name='publicreg'),
    path('authlog/', views.authlog, name='authlog'),
      path('clerkreg/', views.clerkreg, name='clerkreg'),
    path('usrhome/', views.usrhome, name='usrhome'),
    path('applypension/', views.applypension, name='applypension'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('authorityhome/', views.authorityhome, name='authorityhome'),
    path('bank/', views.bank, name='bank'),
    path('deposit/', views.deposit, name='deposit'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('activities/',views.activities,name='activities'),
    path('pensionplan/',views.pensionplan,name='pensionplan'),
    path('pension/',views.pension,name='pension'),
    path('notify/',views.notify,name='notify'),
]+staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
