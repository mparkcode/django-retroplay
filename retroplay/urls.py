"""retroplay URL Configuration

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

# Base urls

from django.contrib import admin
from django.urls import path, include
from products.views import index
from django.views.static import serve
from django.conf import settings
from products import urls as products_urls
from accounts import urls as accounts_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from news import urls as news_urls
from bible import urls as bible_urls
from info import urls as info_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('games/', include(products_urls)),
    path('accounts/', include(accounts_urls)),
    path('cart/', include(cart_urls)),
    path('checkout/', include(checkout_urls)),
    path('news/', include(news_urls)),
    path('bible/', include(bible_urls)),
    path('info/', include(info_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]
