"""wedaidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from wedaidea.views import register
from wedaidea.views import upload
from wedaidea.views import bad
from wedaidea.views import good
from wedaidea.views import login
from wedaidea.views import system
from wedaidea.views import user
from wedaidea.views import download
from wedaidea.views import uploadPage2
from wedaidea.views import report
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('upload/', upload),
    path('bad/', bad),
    path('good/', good),
    path('login/', login),
    path('system/', system),
    path('user/', user),
    path('download/', download),
    path('uploadPage2/', uploadPage2),
    path('uploadPage2/', report),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

