"""bookbee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('era.urls')),
    path('register/', include('era.urls')),
    path('signin/', include('era.urls')),
    path('entry/', include('era.urls')),
    path('enter/', include('era.urls')),
    path('home/', include('era.urls')),
    path('logout/', include('era.urls')),
    path('upload/', include('era.urls')),
    path('upload_book/', include('era.urls')),
    path('booklist/', include('era.urls')),
    path('delete/<int:id>/', include('era.urls')),
    path('update/<int:id>/', include('era.urls')),
    path('added/', include('era.urls')),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
