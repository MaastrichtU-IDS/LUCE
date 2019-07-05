from django.contrib import admin
from django.urls import path

# Import settings to access environment variables 
from django.conf import settings

# Import view functions here
from .views import home_page

from datastore.views import (
	upload_view,
	list_view,
	)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_page),
    path('upload/', upload_view),
    path('browse/', list_view),
    path('my_data/', home_page),
    path('dev/', home_page),
    path('search/', home_page),

]

if settings.DEBUG:
    # Use local simulated CDN
    # Add the following to urlpatterns
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
