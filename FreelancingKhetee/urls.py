"""FreelancingKhetee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from registration.views import UserFormView, MoreInfoView, IndexView, LoginFormView
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', UserFormView.as_view(), name="signup"),
    url(r'^login/', LoginFormView.as_view(), name="login"),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^addinfo/', MoreInfoView.as_view(), name="addinfo"),
    url(r'^logout/$', logout, name='logout'),
]
