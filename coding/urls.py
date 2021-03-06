"""coding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from front import urls as furls
from login import urls as lurls
from backstage import urls as burls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(furls,namespace='front')),
    path('',include(lurls,namespace='login')),
    path('back/',include(burls,namespace='backstage')),
    path('captcha/',include('captcha.urls')),
    path('mdeditor/',include('mdeditor.urls')),
]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
