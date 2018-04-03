"""radio_fm URL Configuration

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

from django.urls import path,re_path
from radio import views


urlpatterns = [
    re_path('^index2$',     views.index2,       name='index2'),
    re_path('',             views.index,        name='index'),

]

#Ссылки на радио
#http://pawno-info.ru/showthread.php?t=280553
#http://sat-life.info/showthread.php?t=6104
#https://www.radiobells.com/radio4site/ ОГРОМНОЕ КОЛИЧЕСТВО ПОТОКОВ
#https://vk.com/topic-103116043_34671966

#Шаблоны
#https://html-templates.info/