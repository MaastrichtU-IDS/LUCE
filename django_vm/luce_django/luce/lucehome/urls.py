from django.contrib import admin
from django.urls import path

# Import settings to access environment variables 
from django.conf import settings

# Import view functions here
from lucehome.views import (
    home_page,
    dev_view
    )

from datastore.views import (
	upload_view,
	browse_view,
    my_data_view,
    detail_view,
    update_view,
    delete_view,
	)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_page),
    path('upload/', upload_view),
    path('browse/', browse_view),
    path('my_data/', my_data_view),
    path('dev/', dev_view),
    path('search/', home_page),

    path('data/<int:dataset_id>/', detail_view),
    path('data/<int:dataset_id>/edit', update_view),
    path('data/<int:dataset_id>/delete', delete_view),
    # re_path(r'^data/(?P<slug>\w+)/$', detail_view)

]

if settings.DEBUG:
    # Use local simulated CDN
    # Add the following to urlpatterns
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
