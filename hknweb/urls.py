"""hknweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create/', users.account_create),
    path('accounts/settings/', users.account_settings),
    path('accounts/activate/', users.activate),
    path('events/', include('hknweb.events.urls')),
    path('alumni/', include('hknweb.alumni.urls')),
    path('tutoring/', include('hknweb.tutoring.urls')),
    path('pages/', include('hknweb.markdown_pages.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('s/', include('hknweb.shortlinks.urls')),
    path('elections/', include('hknweb.elections.urls')),
]
