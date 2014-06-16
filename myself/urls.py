from django.conf.urls import patterns, url
from myself import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *


urlpatterns = patterns('',
	url(r'^$',views.home, name = 'home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
